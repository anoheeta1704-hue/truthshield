# API Contract

## Upload API
POST /upload

Request:
{
  "file": "audio file"
}

Response:
{
  "session_id": "123"
}

---

## Live Analysis
GET /live/:session_id

Response:
{
  "score": 85,
  "status": "good"
}