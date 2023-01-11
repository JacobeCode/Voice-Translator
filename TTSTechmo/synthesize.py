from TTSTechmo.tts.call_synthesize import call_synthesize
from TTSTechmo.address_provider import AddressProvider
from pathlib import Path

def synthesize(settings:object):
    ap = AddressProvider()
    sampling_rate = 44100

    address = ap.get(settings.tts_lang)
    settings.service = address
    call_synthesize(settings, str(settings.text))  # wywołanie generuje plik wav z syntezowanym głosem