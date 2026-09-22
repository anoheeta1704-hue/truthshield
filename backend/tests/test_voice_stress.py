import pytest
from app.services.voice_stress import VoiceStressService, ModelUnavailableError
import os

def test_voice_stress_model_unavailable():
    # Create a fresh service instance
    service = VoiceStressService()
    
    # Temporarily remove model if it somehow exists to test unavailable behavior
    original_model = service.model
    service.model = None

    import io, soundfile as sf, numpy as np
    t = np.linspace(0, 2.0, int(22050 * 2.0), False)
    audio = 0.5 * np.sin(2 * np.pi * 440.0 * t)
    buffer = io.BytesIO()
    sf.write(buffer, audio, 22050, format='WAV', subtype='PCM_16')
    buffer.seek(0)
    valid_buffer = buffer.read()

    with pytest.raises(ModelUnavailableError, match="not trained or available"):
        service.analyze(valid_buffer)

    # Restore
    service.model = original_model
