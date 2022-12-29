# Main file of project
from Text_to_speech.synthesize import synthesize
from Text_to_speech.settings import setup
# Here you can insert the phrase you want to synthesize
settings = setup()
synthesize("Testowanie innych ustawień naszego programu", settings)