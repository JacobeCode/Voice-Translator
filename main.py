# Main file of project
from Text_to_speech.synthesize import synthesize
from Text_to_speech.settings import setup
import sys
from PyQt5 import QtWidgets, uic

from UI import UI

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("VT_ui.ui")
window.show()
app.exec()

# Here you can insert the phrase you want to synthesize
# settings = setup()
# synthesize("Testowanie innych ustawień naszego programu", settings)