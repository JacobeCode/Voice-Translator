# Main file of project - including UI
import sys

from PyQt5 import QtWidgets
from UI.main

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
 