import whisper
import time
import os

class Whisper():
    def __init__(self):
        self.model = whisper.load_model("small", device='cpu')

    def full_transcription(self):
        start = time.time()
        transcription = self.model.transcribe('Whisper/whisper_records/transcribtion.wav')
        end_time = time.time() - start
        return transcription["text"], end_time

model = Whisper()
model.full_transcription()