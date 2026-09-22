import pytest
from fastapi.testclient import TestClient
from app.main import app
import io
import soundfile as sf
import numpy as np

client = TestClient(app)

def create_audio_buffer(duration=2.0, sr=22050, freq=440.0, amplitude=0.5):
    t = np.linspace(0, duration, int(sr * duration), False)
    audio = amplitude * np.sin(2 * np.pi * freq * t)
    buffer = io.BytesIO()
    sf.write(buffer, audio, sr, format='WAV', subtype='PCM_16')
    buffer.seek(0)
    return buffer.read()

def test_analyze_audio_no_file():
    response = client.post("/analyze/audio")
    assert response.status_code == 422 # FastAPI validation error for missing field

def test_analyze_audio_empty_file():
    files = {"file": ("empty.wav", b"")}
    response = client.post("/analyze/audio", files=files)
    assert response.status_code == 400
    assert "Empty file provided" in response.json()["detail"]

def test_analyze_audio_invalid_format():
    files = {"file": ("test.txt", b"this is not a wav file")}
    response = client.post("/analyze/audio", files=files)
    assert response.status_code == 400
    assert "Invalid audio file" in response.json()["detail"]

def test_analyze_audio_model_unavailable():
    # Since we haven't trained the model, sending a valid audio file
    # should return status 200 but indicate model_unavailable in the body
    audio_buffer = create_audio_buffer(duration=2.0)
    files = {"file": ("test.wav", audio_buffer, "audio/wav")}
    response = client.post("/analyze/audio", files=files)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "model_unavailable"
    assert data["stress_score"] is None
    assert "not trained or available" in data["message"]

def test_analyze_audio_short_file():
    audio_buffer = create_audio_buffer(duration=0.5)
    files = {"file": ("short.wav", audio_buffer, "audio/wav")}
    response = client.post("/analyze/audio", files=files)
    
    assert response.status_code == 400
    assert "Audio is too short" in response.json()["detail"]
