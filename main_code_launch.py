# Here is part without GUI - only with 'in-code' settings and synthesis

from TTSTechmo.synthesize import synthesize
from TTSTechmo.settings import setup
from EasyNMT.translator_easynmt import translate
from Whisper.whisper_class import Whisper

settings = setup()
model = Whisper()
# settings.text_to_translate = "Moja wypowiedź testowa"
settings.language_source = 'en'
settings.language = 'pl'

settings.text_to_translate = model.full_transcription()
print("Sentence to translate : " + str(settings.text_to_translate))
settings.text = translate(settings.text_to_translate, settings.language_source, settings.language)
print(settings.text)
if settings.language == 'pl':
    settings.tts_lang = 'tts-pl'
    synthesize(settings)
elif settings.language == 'en':
    settings.tts_lang = 'tts-en'
    synthesize(settings)
else:
    pass
print("Translated sentence : "  + str(settings.text))