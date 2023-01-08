import whisper
import ffmpeg
import pyaudio
import wave

class Whisper():
    def __init__(self):
        self.model = whisper.load_model("medium")
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
    def record(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=self.format,
                        channels=self.channels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)

        print("Start recording")

        frames = []

        try:
            while True:
                data = stream.read(self.chunk)
                frames.append(data)
        except KeyboardInterrupt:
            print("Done recording")
        except Exception as e:
            print(str(e))

        sample_width = p.get_sample_size(self.format)

        stream.stop_stream()
        stream.close()
        p.terminate()

        return sample_width, frames


    def record_to_file(self, file_path):
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(self.channels)
        sample_width, frames = self.record()
        wf.setsampwidth(sample_width)
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    def full_transcription(self):
        print('#' * 80)
        print("Please speak word(s) into the microphone")
        print('Press Ctrl+C to stop the recording')

        self.record_to_file('output.wav')
        transcription = self.model.transcribe('output.wav')

        return transcription["text"]
