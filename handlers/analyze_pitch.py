from fastapi import APIRouter, UploadFile, File


router = APIRouter()

@router.get("/analyze")
async def analyze_pitch(audio_file: UploadFile = File(...)):
    print("hello")