# Main file of project
from Text_to_speech.synthesize import synthesize
from Text_to_speech.settings import setup
import sys
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow, MainWindowPy):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

# Here you can insert the phrase you want to synthesize
# settings = setup()
# synthesize("Sprawdzenie na innym inpucie", settings)
