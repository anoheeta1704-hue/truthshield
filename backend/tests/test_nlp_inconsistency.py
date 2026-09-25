import pytest
from app.services.nlp_inconsistency import NLPInconsistencyService, NLPUnavailableError

def test_split_statements():
    service = NLPInconsistencyService()
    text = "The quick brown fox. Jumped over the lazy dog! What a sight."
    statements = service.split_into_statements(text)
    assert len(statements) == 3
    assert statements[0] == "The quick brown fox."
    assert statements[1] == "Jumped over the lazy dog!"
    assert statements[2] == "What a sight."

def test_analyze_empty_text():
    service = NLPInconsistencyService()
    with pytest.raises(ValueError, match="Empty text"):
        service.analyze_text("")
    with pytest.raises(ValueError, match="Empty text"):
        service.analyze_text("   ")

def test_nlp_model_unavailable():
    service = NLPInconsistencyService()
    
    # Force model unavailable
    original_model = service.classifier
    service.classifier = None

    with pytest.raises(NLPUnavailableError, match="model is not available"):
        service.analyze_text("Statement 1. Statement 2.")
        
    service.classifier = original_model
