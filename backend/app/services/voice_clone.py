"""
Voice Clone Detection Service

Analyzes audio for characteristics associated with synthetic or cloned speech.

Technologies:
  - Librosa: Audio feature extraction (FFT/STFT-based spectral analysis)
  - RawNet2 / ASVspoof: Pretrained deepfake/spoofing detection model

Model Weights Setup:
  - RawNet2/ASVspoof pretrained weights are NOT included in this repository.
  - Place pretrained weights in: backend/models/voice_clone/
  - Without weights, this service will return a placeholder response
    indicating that the model is not yet configured.
  - See Milestone 6 documentation for exact weight format and source details.
  - Do NOT commit model weights to git (they are in .gitignore).

Output: Voice clone probability (0.0 to 1.0)

IMPORTANT: This is an AI-generated probability, NOT definitive detection.

Implementation: Milestone 6 (Voice Clone Detection)
"""
