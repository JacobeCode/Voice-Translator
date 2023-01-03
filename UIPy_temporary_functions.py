from Text_to_speech.synthesize import synthesize
from Text_to_speech.settings import setup

def SynthesisFunction(self):
    settings = setup()
    synthesize("Nowe środowisko", settings)