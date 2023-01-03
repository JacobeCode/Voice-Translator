# Main file of project
from Text_to_speech.synthesize import synthesize
from Text_to_speech.settings import setup
import sys
from UI import Ui_MainWindow
from PyQt5 import QtWidgets, uic

from UI import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()

# Here you can insert the phrase you want to synthesize
# settings = setup()
# synthesize("Sprawdzenie na innym inpucie", settings)
