import pytest
import io
import soundfile as sf
import numpy as np
from app.services.feature_extraction import extract_features

def create_audio_buffer(duration=2.0, sr=22050, freq=440.0, amplitude=0.5):
    """Helper to create a valid WAV file buffer."""
    t = np.linspace(0, duration, int(sr * duration), False)
    audio = amplitude * np.sin(2 * np.pi * freq * t)
    
    buffer = io.BytesIO()
    sf.write(buffer, audio, sr, format='WAV', subtype='PCM_16')
    buffer.seek(0)
    return buffer.read()

def test_extract_features_valid_audio():
    audio_buffer = create_audio_buffer(duration=2.0)
    features = extract_features(audio_buffer)
    assert features is not None
    assert len(features) == 17 # 13 MFCC + 1 Pitch + 1 ZCR + 1 Jitter + 1 Shimmer

def test_extract_features_too_short():
    # Less than 1 second
    audio_buffer = create_audio_buffer(duration=0.5)
    with pytest.raises(ValueError, match="Audio is too short"):
        extract_features(audio_buffer)

def test_extract_features_silence_only():
    # Amplitude 0
    audio_buffer = create_audio_buffer(amplitude=0.0)
    with pytest.raises(ValueError, match="Audio contains only silence"):
        extract_features(audio_buffer)
