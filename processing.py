import cv2
import numpy as np
import moviepy.editor as mp
import os
from insightface.app import FaceAnalysis

BASE = "/content/drive/MyDrive/video_extract_api"

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0, det_size=(640,640))  # GPU support

def get_embedding(img):
    faces = app.get(img)
    if not faces:
        return None
    emb = faces[0].embedding
    return emb / np.linalg.norm(emb)

def process_video(video_path, ref_path, output_path, step=0.5, threshold=0.55):
    try:
        ref_img = cv2.imread(ref_path)
        ref_embedding = get_embedding(ref_img)

        if ref_embedding is None:
            raise ValueError("❌ No face detected in reference image")

        clip = mp.VideoFileClip(video_path)
        detected = []

        t = 0
        while t < clip.duration:
            frame = clip.get_frame(t)
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            faces = app.get(frame_bgr)

            match = False
            for f in faces:
                emb = f.embedding / np.linalg.norm(f.embedding)
                sim = np.dot(emb, ref_embedding)
                if sim > threshold:
                    match = True
                    break

            if match:
                detected.append(t)

            t += step

        if not detected:
            return False

        scenes = []
        start = detected[0]
        end = detected[0]

        for ts in detected[1:]:
            if ts - end <= step + 0.1:
                end = ts
            else:
                scenes.append((start, end))
                start = end = ts
        scenes.append((start, end))

        clips = []
        for s, e in scenes:
            clips.append(clip.subclip(max(0, s-0.3), min(clip.duration, e+0.3)))

        final = mp.concatenate_videoclips(clips)
        final.write_videofile(output_path, codec="libx264")

        return True

    except Exception as e:
        print("ERROR:", e)
        return False
