# 🎥 Video Face Extractor API

This project extracts and merges all video segments where a specific person appears.  
A reference image of the target face is uploaded, and the system automatically detects and clips matching segments from the main video.

---

## 🚀 Features
✅ FastAPI-based REST API  
✅ Face detection using InsightFace (buffalo_l model)  
✅ Automatic scene segmentation  
✅ Clips merged into a single downloadable result video  
✅ Supports MP4 and image uploads  
✅ Web UI for easy usage (index.html)

---

## 📁 Project Structure

video_extract_api/
│
├─ templates/                  # HTML UI files
│  ├─ index.html
│  └─ results.html (optional)
│
├─ uploads/                    # Video uploads (runtime)
├─ refer/                      # Reference face images (runtime)
├─ output/                     # Extracted result
│
├─ main.py                     # FastAPI app
├─ processing.py               # Video processing logic
├─ requirements.txt
└─ README.md


yaml
Copy code

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Backend API | FastAPI |
| Face Recognition | InsightFace |
| Video Processing | MoviePy, OpenCV |
| UI Template | Jinja2 HTML |
| Hosting (tested on) | Google Colab + Ngrok |

---

## 🔥 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web form UI |
| POST | `/process` | Upload video + reference face → process |
| GET | `/download` | Download result video |

---

## 🛠️ How to Run in Google Colab

1️⃣ Mount Drive & Install dependencies

```bash
!pip install fastapi uvicorn python-multipart moviepy insightface onnxruntime opencv-python-headless
2️⃣ Run FastAPI server

bash
Copy code
!uvicorn main:app --host 0.0.0.0 --port 8000
3️⃣ Expose API using ngrok (optional)

bash
Copy code
!ngrok http 8000
Then open the generated URL ✅

📌 Future Enhancements
✔ Improve UI
✔ Add face preview thumbnails
✔ Support multiple face selection
✔ Docker containerization for deployment

📄 License
This project is for educational / demo purposes.

👨‍💻 Author
Puli Eswar
Video Extraction & AI Processing Developer

📌 GitHub: https://github.com/Eswarpuli

If you like this project, ⭐ the repository!

yaml
Copy code

---

✅ You can now commit this README.md to your GitHub repo.

Would you like me to:

✅ Add project demo screenshot placeholders?  
✅ Add a polished project description in GitHub sidebar?  
✅ Help you deploy this API as a public web app?  

Just tell me — I’m here to help! 🚀
