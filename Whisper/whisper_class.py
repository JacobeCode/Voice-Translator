import whisper
import time

class Whisper():
    def __init__(self):
        self.model = whisper.load_model("small", device='cuda')

    def full_transcription(self):
        start = time.time()
        transcription = self.model.transcribe('output.wav')
        end_time = time.time() - start
        return transcription["text"], end_time
