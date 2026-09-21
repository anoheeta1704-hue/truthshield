"""
NLP Inconsistency Detection Service

Converts speech to text and analyzes the transcript for linguistic inconsistencies.

Pipeline:
  Audio → Speech-to-Text (faster-whisper) → Transcript → NLP Analysis → Score

Technologies:
  - faster-whisper: Speech-to-text transcription
    Model will be downloaded on first use and cached.
  - Transformers + RoBERTa/NLI: Natural Language Inference for inconsistency detection
    Uses a pretrained NLI model to identify contradictions within the transcript.

Output:
  - Inconsistency score: 0.0 to 1.0
  - Transcript: Full text from speech-to-text
  - Analysis: Supporting textual analysis / flagged segments

IMPORTANT: This is an AI-generated indicator, NOT definitive detection of deception.

Implementation: Milestone 5 (NLP Inconsistency Detection)
"""
