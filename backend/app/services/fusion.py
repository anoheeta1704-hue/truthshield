"""
Score Fusion Service — CENTRALIZED

Combines analysis scores from all three services into a unified result.
This logic MUST remain centralized. Do not duplicate weighting elsewhere.

Weights:
  voice_stress       = 0.35
  nlp_inconsistency  = 0.35
  voice_clone        = 0.30

Formula:
  final_score = (0.35 * voice_stress) + (0.35 * nlp_inconsistency) + (0.30 * voice_clone)

Fraud Alert Override:
  If voice_clone_probability > 0.90, trigger a fraud alert
  regardless of other scores.

Output:
  - final_score: Weighted combination (0.0 to 1.0)
  - fraud_alert: Boolean flag

Implementation: Milestone 7 (Score Fusion)
"""
