from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.services.voice_stress import voice_stress_service, ModelUnavailableError

router = APIRouter()

class AnalysisResponse(BaseModel):
    stress_score: float | None = None
    status: str
    message: str | None = None

@router.post("/audio", response_model=AnalysisResponse)
async def analyze_audio(file: UploadFile = File(...)):
    """
    Voice stress analysis endpoint (Milestone 3).
    Expects an audio file via multipart/form-data.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    # Read the file into memory
    audio_buffer = await file.read()

    if not audio_buffer:
        raise HTTPException(status_code=400, detail="Empty file provided")

    try:
        # Perform analysis
        result = voice_stress_service.analyze(audio_buffer)
        return AnalysisResponse(
            stress_score=result["score"],
            status="success"
        )
    except ModelUnavailableError as e:
        return AnalysisResponse(
            status="model_unavailable",
            message=str(e)
        )
    except ValueError as e:
        # Catch exceptions like "Audio is too short" or "Audio contains only silence"
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Catch librosa/soundfile decoding errors (invalid audio format)
        raise HTTPException(status_code=400, detail=f"Invalid audio file: {str(e)}")
