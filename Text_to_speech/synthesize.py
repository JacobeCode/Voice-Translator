from argparse_options import tts_args
from tts.call_synthesize import call_synthesize
from address_provider import AddressProvider
from pathlib import Path

def synthesize():
    ap = AddressProvider()
    sampling_rate = 44100

    address = ap.get("tts-pl")
    input_text = "Test zmiany próbny funkcja ciekawe kiedy działa i czy teraz też, wywalone"
    tts_args_pl = tts_args(address, input_text, output_path="TTS_PL.wav")
    call_synthesize(tts_args_pl, input_text)  # wywołanie generuje plik wav z syntezowanym głosem