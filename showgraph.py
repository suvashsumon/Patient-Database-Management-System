from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/showgraph.ui", self)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = QApplication([])
window = UI()
window.location_on_the_screen()
window.show()
app.exec_()
