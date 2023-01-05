from UI import UIPy_MainWindow

from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, UIPy_MainWindow.Ui_Voice_Translator):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)