# API Contract

## System
`GET /health`
Returns service health status.

## Analysis Endpoints
`POST /analyze/audio`
Voice stress analysis (Milestone 3).

`POST /analyze/text`
NLP inconsistency detection pipeline (Milestone 4).
Accepts JSON: `{"text": "your statements here"}`
Returns:
```json
{
  "status": "success",
  "inconsistency_probability": 0.72,
  "statements": ["..."],
  "contradictions": [{"statement_1": "...", "statement_2": "...", "score": 0.9}]
}
```

`POST /analyze/audio-nlp`
Audio-to-text NLP inconsistency detection pipeline (Milestone 4).
Accepts multipart/form-data with an audio file.
Returns the same response as `/analyze/text` but includes the `transcript`.

*Pipeline Architecture:*
Audio → faster-whisper → transcript → NLI model (cross-encoder/nli-deberta-v3-small) → inconsistency probability.

*Model Unavailable Behavior:*
If the model cannot be loaded or is not downloaded yet, the endpoint gracefully returns:
```json
{
  "status": "model_unavailable",
  "message": "NLP model is not available."
}
```
`POST /analyze/voice-clone`
Voice clone detection (Milestone 6).

`POST /analyze/full`
Full analysis pipeline with score fusion (Milestone 7).

*All analysis endpoints accept multipart/form-data with an audio file.*

## Session Management
`GET /sessions`
Retrieve analysis session history (Milestone 9).

## Live Streaming
`POST /stream/chunk`
Process an audio chunk from live browser recording (Milestone 10).