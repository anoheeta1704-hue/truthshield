import os
import json
import numpy as np
import xgboost as xgb
from app.services.feature_extraction import extract_features

# The path where the trained model should be stored
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "voice_stress_xgb.json")

class ModelUnavailableError(Exception):
    """Raised when the pretrained model is not available."""
    pass

class VoiceStressService:
    def __init__(self):
        self.model = None
        self._load_model()

    def _load_model(self):
        """Loads the XGBoost model if it exists."""
        if os.path.exists(MODEL_PATH):
            self.model = xgb.XGBClassifier()
            self.model.load_model(MODEL_PATH)
        else:
            self.model = None

    def is_model_available(self) -> bool:
        return self.model is not None

    def analyze(self, audio_buffer: bytes) -> dict:
        """
        Analyzes the audio buffer for voice stress.
        Returns a dictionary with the analysis score.
        """
        # Extract features first (this validates the audio)
        features = extract_features(audio_buffer)

        if not self.is_model_available():
            raise ModelUnavailableError("The voice stress model is not trained or available.")

        # XGBoost expects 2D array: (n_samples, n_features)
        X = features.reshape(1, -1)

        # Predict probability of class 1 (Stress)
        prob = self.model.predict_proba(X)[0][1]

        return {
            "score": float(prob),
            "status": "success"
        }

# Singleton instance
voice_stress_service = VoiceStressService()
