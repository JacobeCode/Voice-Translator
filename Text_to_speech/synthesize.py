from Text_to_speech.argparse_options import tts_args
from Text_to_speech.tts.call_synthesize import call_synthesize
from Text_to_speech.address_provider import AddressProvider
from pathlib import Path

def synthesize(input_text):
    ap = AddressProvider()
    sampling_rate = 44100

    address = ap.get("tts-pl")
    tts_args_pl = tts_args(address, input_text, output_path="TTS_PL.wav")
    call_synthesize(tts_args_pl, input_text)  # wywołanie generuje plik wav z syntezowanym głosem