import io
import os
import tempfile

try:
    from faster_whisper import WhisperModel
    _HAS_WHISPER = True
except ImportError:
    _HAS_WHISPER = False

class TranscriptionError(Exception):
    """Raised when transcription fails."""
    pass

class TranscriptionService:
    def __init__(self):
        self.model = None
        self._load_model()

    def _load_model(self):
        try:
            if not _HAS_WHISPER:
                self.model = None
                return
                
            # Load tiny model for speed in local dev
            self.model = WhisperModel("tiny", device="cpu", compute_type="int8")
        except Exception as e:
            self.model = None
            print(f"Failed to load faster-whisper model: {e}")

    def is_model_available(self) -> bool:
        return self.model is not None

    def transcribe_audio(self, audio_buffer: bytes) -> dict:
        if not self.is_model_available():
            raise TranscriptionError("Transcription model is not available.")

        # faster-whisper needs a file path or a file-like object.
        # We write to a temporary file since passing bytes directly can be finicky with some audio formats
        temp_path = ""
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                temp_file.write(audio_buffer)
                temp_path = temp_file.name

            segments, info = self.model.transcribe(temp_path, beam_size=5)
            
            transcript = " ".join([segment.text for segment in segments]).strip()
            
            return {
                "text": transcript,
                "language": info.language,
                "language_probability": info.language_probability
            }
        except Exception as e:
            raise TranscriptionError(f"Error during transcription: {e}")
        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)

transcription_service = TranscriptionService()
