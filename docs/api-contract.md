# API Contract

## System
`GET /health`
Returns service health status.

## Analysis Endpoints
`POST /analyze/audio`
Voice stress analysis (Milestone 3).

`POST /analyze/text`
NLP inconsistency detection (Milestone 5).

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