from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from detect import detect_pitch as dp
import tempfile


router = APIRouter()

@router.get("/analyze/file")
async def analyze_pitch(audio_file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        contents = await audio_file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    try:
        notes = dp.detect_pitch(tmp_path)

        return JSONResponse(content={"notes": notes})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
        