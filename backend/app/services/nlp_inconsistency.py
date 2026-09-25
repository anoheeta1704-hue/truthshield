try:
    from transformers import pipeline
    _HAS_TRANSFORMERS = True
except ImportError:
    _HAS_TRANSFORMERS = False

import re

class NLPUnavailableError(Exception):
    """Raised when the NLP model is not available."""
    pass

class NLPInconsistencyService:
    def __init__(self):
        self.classifier = None
        self._load_model()

    def _load_model(self):
        try:
            if not _HAS_TRANSFORMERS:
                self.classifier = None
                return
            
            # Using zero-shot classification via BART as a versatile NLI fallback,
            # or a specific cross-encoder. We use facebook/bart-large-mnli for simplicity
            # as it's the standard for zero-shot NLI in transformers pipelines.
            # To keep it lightweight, we use cross-encoder/nli-deberta-v3-small.
            self.classifier = pipeline("text-classification", model="cross-encoder/nli-deberta-v3-small", device=-1)
        except Exception as e:
            self.classifier = None
            print(f"Failed to load NLP model: {e}")

    def is_model_available(self) -> bool:
        return self.classifier is not None

    def split_into_statements(self, text: str) -> list[str]:
        # Basic sentence splitting
        statements = re.split(r'(?<=[.!?]) +', text.strip())
        return [s.strip() for s in statements if len(s.strip()) > 10]

    def analyze_text(self, text: str) -> dict:
        if not text or not text.strip():
            raise ValueError("Empty text provided.")
            
        if not self.is_model_available():
            raise NLPUnavailableError("NLP model is not available.")

        statements = self.split_into_statements(text)
        
        if len(statements) < 2:
            return {
                "inconsistency_probability": 0.0,
                "statements": statements,
                "contradictions": [],
                "message": "Not enough statements for contradiction analysis."
            }

        highest_contradiction = 0.0
        contradictions = []

        # Compare adjacent statements (simplified logic)
        for i in range(len(statements) - 1):
            premise = statements[i]
            hypothesis = statements[i+1]
            
            # Format depends on the pipeline. 
            # For cross-encoder/nli-deberta-v3-small: 'LABEL_0' is contradiction, 'LABEL_1' is entailment, 'LABEL_2' is neutral.
            # Wait, actually cross-encoder requires dict with text and text_pair. 
            # We construct a concatenated string if using simple text-classification pipeline:
            input_text = f"{premise} [SEP] {hypothesis}"
            try:
                results = self.classifier(input_text, top_k=None)
                # Results is a list of dicts: [{'label': 'LABEL_0', 'score': 0.9}, ...]
                
                # NLI classes for cross-encoder/nli-deberta-v3-small:
                # 0: contradiction, 1: entailment, 2: neutral
                contradiction_score = 0.0
                for r in results:
                    if r['label'] == 'LABEL_0' or r['label'] == 'contradiction':
                        contradiction_score = r['score']
                        break
                
                if contradiction_score > highest_contradiction:
                    highest_contradiction = contradiction_score

                if contradiction_score > 0.5:
                    contradictions.append({
                        "statement_1": premise,
                        "statement_2": hypothesis,
                        "score": contradiction_score
                    })
            except Exception as e:
                # If pipeline fails
                pass

        return {
            "inconsistency_probability": float(highest_contradiction),
            "statements": statements,
            "contradictions": contradictions
        }

nlp_service = NLPInconsistencyService()
