import pytest
from app.services.transcription import TranscriptionService, TranscriptionError

def test_transcription_model_unavailable():
    service = TranscriptionService()
    
    # Force model unavailable
    original_model = service.model
    service.model = None

    with pytest.raises(TranscriptionError, match="model is not available"):
        service.transcribe_audio(b"fake_buffer")
        
    service.model = original_model
