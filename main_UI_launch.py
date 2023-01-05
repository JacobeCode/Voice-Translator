# Main file of project - including UI
import sys

from PyQt5 import QtWidgets
from UI.main_window_class import MainWindow

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
 