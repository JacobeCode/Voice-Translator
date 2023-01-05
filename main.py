# Main file of project
import sys
import UIPy_MainWindow

from Text_to_speech.synthesize import synthesize
from Text_to_speech.settings import setup
from PyQt5 import QtWidgets

# Class of UI_Main_Window - for tests exists here - after this will be deployed to toher .py file
class MainWindow(QtWidgets.QMainWindow, UIPy_MainWindow.Ui_Voice_Translator):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()

# Here is part without GUI - only with 'in-code' settings and synthesis
# settings = setup()
# synthesize("Taki szybki test", settings)
 