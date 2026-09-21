"""
Session Management Endpoints

GET /sessions — Retrieve analysis session history from PostgreSQL.

Response:
  {
    "sessions": [
      {
        "session_id": "uuid",
        "created_at": "ISO8601",
        "final_score": 0.0,
        "fraud_alert": false
      }
    ]
  }

Implementation: Milestone 9 (PostgreSQL & Session History)
"""
