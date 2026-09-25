import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_text_empty():
    response = client.post("/analyze/text", json={"text": ""})
    assert response.status_code == 400
    assert "Empty text" in response.json()["detail"]

def test_analyze_text_whitespace():
    response = client.post("/analyze/text", json={"text": "   "})
    assert response.status_code == 400
    assert "Empty text" in response.json()["detail"]

def test_analyze_text_single_statement():
    response = client.post("/analyze/text", json={"text": "This is a single statement."})
    assert response.status_code == 200
    data = response.json()
    
    # Depending on model availability, it might be success or model_unavailable
    if data["status"] == "success":
        assert data["inconsistency_probability"] == 0.0
        assert len(data["statements"]) == 1
        assert len(data["contradictions"]) == 0
    else:
        assert data["status"] == "model_unavailable"

def test_analyze_audio_nlp_empty_file():
    files = {"file": ("empty.wav", b"")}
    response = client.post("/analyze/audio-nlp", files=files)
    assert response.status_code == 400
    assert "Empty file provided" in response.json()["detail"]
