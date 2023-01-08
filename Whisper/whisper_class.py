import whisper
import ffmpeg
import pyaudio
import wave

class Whisper():
    def __init__(self):
        self.model = whisper.load_model("small", device='cuda')

    def full_transcription(self):
        transcription = self.model.transcribe('output.wav')

        return transcription["text"]
