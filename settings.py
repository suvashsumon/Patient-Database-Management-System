from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("setting.ui", self)


app = QApplication([])
window = UI()
window.show()
app.exec_()
