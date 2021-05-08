from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys


class Addrecord(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/addrecord.ui", self)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# app = QApplication([])
# window = Addrecord()
# window.location_on_the_screen()
# window.show()
# app.exec_()
