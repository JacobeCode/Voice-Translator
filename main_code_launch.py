# Here is part without GUI - only with 'in-code' settings and synthesis

from TTSTechmo.synthesize import synthesize
from TTSTechmo.settings import setup
from EasyNMT.translator_easynmt import translate

settings = setup()
settings.text_to_translate = "Testowanie wejścia kodu"
settings.language_source = 'pl'
settings.language = 'en'

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

