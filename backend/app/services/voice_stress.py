"""
Voice Stress Analysis Service

Analyzes acoustic characteristics of speech to identify stress-related patterns.

Dataset: RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)
  - Place the RAVDESS dataset in: backend/data/ravdess/
  - Expected structure: Actor_XX/ directories containing .wav files
  - Download from: https://zenodo.org/record/1188976
  - Do NOT commit the dataset to git (it is in .gitignore).

Audio Processing: Librosa

Features to extract:
  - MFCC (Mel-Frequency Cepstral Coefficients)
  - Pitch (Fundamental Frequency F0)
  - Jitter (Pitch perturbation)
  - Shimmer (Amplitude perturbation)
  - Zero Crossing Rate (ZCR)

Model: XGBoost classifier
  - Trained model saved to: backend/models/voice_stress_xgb.json
  - Training script: TBD in Milestone 3

Output: Normalized stress score (0.0 to 1.0)

IMPORTANT: This is an AI-assisted signal indicator, NOT definitive proof of deception.
The system must describe results as probabilities and indicators.

Implementation: Milestone 3 (Voice Stress Analysis)
"""
