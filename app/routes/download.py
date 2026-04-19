from fastapi import APIRouter
from pydantic import BaseModel
from app.services.downloader import get_video_data

router = APIRouter()

class DownloadRequest(BaseModel):
    url: str

@router.post("/download")
def download_video(req: DownloadRequest):
    try:
        data = get_video_data(req.url)
        return data
    except Exception:
        return {"error": "Failed to fetch video"}
