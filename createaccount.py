from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("createaccount.ui", self)

    def location_on_the_screen(self):
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

app = QApplication([])
window = UI()
window.location_on_the_screen()
window.show()
app.exec_()
