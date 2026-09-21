"""
Analysis Endpoints

POST /analyze/audio       — Voice stress analysis (Milestone 3)
POST /analyze/text        — NLP inconsistency detection (Milestone 5)
POST /analyze/voice-clone — Voice clone detection (Milestone 6)
POST /analyze/full        — Full analysis pipeline with score fusion (Milestone 7)

Each endpoint accepts multipart/form-data with an audio file
and returns JSON with analysis scores and metadata.
"""
