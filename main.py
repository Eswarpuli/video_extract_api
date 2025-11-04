from fastapi import FastAPI, UploadFile, File, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import shutil, os
from processing import process_video

BASE = "/content/drive/MyDrive/video_extract_api"
templates = Jinja2Templates(directory=os.path.join(BASE, "templates"))

app = FastAPI(title="Video Face Extractor")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, message: str = None):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": message
    })

@app.post("/process")
async def process(
    request: Request,
    background_tasks: BackgroundTasks,
    video: UploadFile = File(...),
    ref_img: UploadFile = File(...)
):
    video_path = os.path.join(BASE, "uploads", video.filename)
    ref_path = os.path.join(BASE, "refer", ref_img.filename)

    file_name, _ = os.path.splitext(video.filename)
    output_filename = f"{file_name}_result.mp4"
    output_path = os.path.join(BASE, "output", output_filename)

    with open(video_path, "wb") as f:
        shutil.copyfileobj(video.file, f)
    with open(ref_path, "wb") as f:
        shutil.copyfileobj(ref_img.file, f)

    background_tasks.add_task(process_video, video_path, ref_path, output_path)

    return RedirectResponse(
        url="/?message=✅ Processing started! Refresh in a minute...",
        status_code=303
    )


@app.get("/results", response_class=HTMLResponse)
def show_results(request: Request):
    files = os.listdir(os.path.join(BASE, "output"))
    return templates.TemplateResponse("results.html", {
        "request": request,
        "files": files
    })


@app.get("/download/{filename}")
def download(filename: str):
    path = os.path.join(BASE, "output", filename)
    if not os.path.exists(path):
        return {"error": "File not found"}
    return FileResponse(path, media_type="video/mp4", filename=filename)
