# Here is part without GUI - only with 'in-code' settings and synthesis

from TTSTechmo.synthesize import synthesize
from TTSTechmo.settings import setup

settings = setup()
synthesize("Taki szybki test", settings)
