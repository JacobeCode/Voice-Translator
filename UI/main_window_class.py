from UI import main_window

from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, main_window.Ui_Voice_Translator):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)