# TruthShield Project Specification

## 1. Project Overview

TruthShield is an AI-based audio deception analysis system.

The system analyzes audio conversations using multiple AI/ML signals and combines them into a unified analysis result.

The project is being developed by a single developer.

The MVP should focus on building a working end-to-end system rather than unnecessary complexity.

---

# 2. Core Analysis Components

TruthShield will contain three primary analysis components:

## A. Voice Stress Analysis

Analyze acoustic characteristics of speech to identify stress-related patterns.

Planned approach:

- Dataset: RAVDESS
- Audio processing: Librosa
- Features:
  - MFCC
  - Pitch
  - Jitter
  - Shimmer
  - Zero Crossing Rate
- Model:
  - XGBoost

The model should produce a normalized score that can be used by the fusion layer.

Important:

The system must describe this as an AI-assisted signal and not as definitive proof that a person is lying.

---

## B. NLP Inconsistency Detection

Convert speech to text and analyze the transcript for linguistic inconsistency.

Planned pipeline:

Audio
→ Speech-to-text
→ Transcript
→ NLP analysis
→ Inconsistency score

Technologies:

- faster-whisper
- Transformers
- pretrained RoBERTa/NLI-style model

The system should return an inconsistency score and supporting analysis.

---

## C. Voice Clone Detection

Analyze audio for characteristics associated with synthetic or cloned speech.

Planned approach:

- Librosa
- FFT/STFT-based audio analysis
- pretrained RawNet2 / ASVspoof weights

The system should produce a voice-clone probability.

---

# 3. Score Fusion

The three analysis scores should be combined using:

voice_stress = 0.35

nlp_inconsistency = 0.35

voice_clone = 0.30

Final score:

final_score =
    0.35 * voice_stress +
    0.35 * nlp_inconsistency +
    0.30 * voice_clone

Fraud alert override:

If voice_clone_probability > 0.90,
trigger a fraud alert.

The fusion logic should be implemented centrally so that the weighting is not duplicated throughout the application.

---

# 4. Frontend

Frontend technology:

- React
- Vite
- Tailwind CSS
- Zustand
- React Router
- Lucide React

Planned frontend features:

- Audio upload
- Analysis dashboard
- Truth meter / overall score
- Analysis breakdown
- Fraud alert
- Session history
- Live recording

Planned components include:

- MediaUploader
- TruthMeterGauge
- BreakdownPanel
- FraudAlertBanner
- SessionHistory
- LiveRecord

---

# 5. Backend

Backend technology:

- Python
- FastAPI

The backend should expose REST APIs for analysis and session management.

Planned endpoints:

GET /health

POST /analyze/audio

POST /analyze/text

POST /analyze/voice-clone

POST /analyze/full

GET /sessions

POST /stream/chunk

---

# 6. Database

Planned database:

- PostgreSQL

Database functionality:

- Store analysis sessions
- Store timestamps
- Store scores
- Store analysis results
- Retrieve previous sessions

SQLAlchemy should be used for database interaction.

---

# 7. Redis

Redis may be used for:

- temporary processing state
- caching
- live analysis support

Do not introduce Redis complexity until it is actually required by the implementation.

---

# 8. Live Analysis

Live recording should use the browser's MediaRecorder API.

The browser should record audio in approximately 10-second chunks.

The chunks can then be sent to:

POST /stream/chunk

Do not introduce WebRTC or Kafka for the MVP.

---

# 9. Project Architecture

The intended architecture is:

React Frontend
        ↓
FastAPI Backend
        ↓
Analysis Services
        ├── Voice Stress
        ├── NLP Inconsistency
        └── Voice Clone Detection
        ↓
Score Fusion
        ↓
PostgreSQL / Redis

Keep frontend and backend clearly separated.

---

# 10. Development Principles

This is a solo project.

Therefore:

1. Build incrementally.
2. Do not implement the entire project in one step.
3. Complete and test one milestone before moving to the next.
4. Prefer simple maintainable architecture.
5. Avoid unnecessary technologies.
6. Reuse pretrained models where specified.
7. Do not hard-code secrets.
8. Use environment variables for configuration.
9. Add error handling.
10. Add basic tests for important functionality.
11. Keep the frontend and backend modular.
12. Do not claim that the system can definitively determine whether someone is lying.
13. Analysis results should be presented as AI-generated indicators/probabilities.

---

# 11. Testing Requirements

The system should eventually test:

- Empty audio
- Very short audio
- Silence-only audio
- Invalid audio files
- Empty text
- Invalid API requests
- Individual model outputs
- Full pipeline
- Score fusion
- Fraud alert threshold
- Database operations
- API response handling
- Frontend error states

---

# 12. Deployment Target

Planned deployment:

Frontend:
Vercel

Backend:
Railway or Render

Database:
Managed PostgreSQL

Redis:
Managed Redis if required

---

# 13. Current Repository Status

The current repository is an initial React/Vite application.

Existing frontend pages include:

- Upload
- Live
- History

These pages may currently contain placeholder implementations.

The existing project must be inspected before modifying it.

Do not assume that functionality exists merely because a file or component name exists.

---

# 14. Development Order

Implement the project in this order:

1. Repository analysis and architecture
2. Backend foundation
3. Voice stress analysis
4. Frontend audio upload
5. NLP inconsistency detection
6. Voice clone detection
7. Score fusion
8. Complete analysis dashboard
9. PostgreSQL and session history
10. Live recording
11. Testing
12. Deployment

Do not skip ahead unless explicitly instructed.