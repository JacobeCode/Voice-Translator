import whisper
import ffmpeg
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def record():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start recording")

    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))

    sample_width = p.get_sample_size(FORMAT)

    stream.stop_stream()
    stream.close()
    p.terminate()

    return sample_width, frames


def record_to_file(file_path):
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


model = whisper.load_model("tiny")


def transcribe(audio):
    transcription = model.transcribe(audio)

    return transcription["text"]


def full_transcription():
    print('#' * 80)
    print("Please speak word(s) into the microphone")
    print('Press Ctrl+C to stop the recording')

    record_to_file('output.wav')

    transcription = model.transcribe('output.wav')

    return transcription["text"]


if __name__ == '__main__':
    print(translation())
