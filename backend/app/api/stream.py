"""
Live Streaming Endpoint

POST /stream/chunk — Process an audio chunk from live browser recording.

The browser records audio in ~10-second chunks using MediaRecorder API
and sends each chunk to this endpoint for progressive analysis.

Request: multipart/form-data
  - chunk: Audio data (~10 seconds, WebM/Opus format)
  - session_id: Session identifier (optional; creates new session if omitted)

Response:
  {
    "session_id": "uuid",
    "chunk_index": 0,
    "partial_score": 0.0
  }

Note: Do not introduce WebRTC or Kafka for the MVP.

Implementation: Milestone 10 (Live Recording)
"""
