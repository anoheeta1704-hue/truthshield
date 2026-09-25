from fastapi import APIRouter, UploadFile, File, HTTPException, Body
from pydantic import BaseModel
from app.services.voice_stress import voice_stress_service, ModelUnavailableError
from app.services.transcription import transcription_service, TranscriptionError
from app.services.nlp_inconsistency import nlp_service, NLPUnavailableError

router = APIRouter()

class AnalysisResponse(BaseModel):
    stress_score: float | None = None
    status: str
    message: str | None = None

class NLPTextRequest(BaseModel):
    text: str

class NLPResponse(BaseModel):
    status: str
    inconsistency_probability: float | None = None
    statements: list[str] | None = None
    contradictions: list[dict] | None = None
    message: str | None = None
    transcript: str | None = None

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

@router.post("/text", response_model=NLPResponse)
async def analyze_text(request: NLPTextRequest):
    """
    NLP inconsistency analysis endpoint (Milestone 4).
    Expects JSON with a 'text' field.
    """
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Empty text provided")

    try:
        result = nlp_service.analyze_text(request.text)
        return NLPResponse(
            status="success",
            inconsistency_probability=result["inconsistency_probability"],
            statements=result["statements"],
            contradictions=result["contradictions"]
        )
    except NLPUnavailableError as e:
        return NLPResponse(status="model_unavailable", message=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/audio-nlp", response_model=NLPResponse)
async def analyze_audio_nlp(file: UploadFile = File(...)):
    """
    Audio -> Transcript -> NLP inconsistency analysis endpoint (Milestone 4).
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    audio_buffer = await file.read()
    if not audio_buffer:
        raise HTTPException(status_code=400, detail="Empty file provided")

    # 1. Transcription
    try:
        transcription_result = transcription_service.transcribe_audio(audio_buffer)
        transcript = transcription_result["text"]
    except TranscriptionError as e:
        return NLPResponse(status="model_unavailable", message=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid audio or transcription error: {str(e)}")

    if not transcript or not transcript.strip():
        raise HTTPException(status_code=400, detail="No speech detected in audio")

    # 2. NLP Analysis
    try:
        result = nlp_service.analyze_text(transcript)
        return NLPResponse(
            status="success",
            inconsistency_probability=result["inconsistency_probability"],
            statements=result["statements"],
            contradictions=result["contradictions"],
            transcript=transcript
        )
    except NLPUnavailableError as e:
        return NLPResponse(status="model_unavailable", message=str(e), transcript=transcript)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
