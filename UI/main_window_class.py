from UI import main_window

from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, main_window.Ui_main_window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)