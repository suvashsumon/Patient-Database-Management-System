from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dashboard.ui", self)

        # add button
        addbutton = self.findChild(QPushButton, 'addrecord')
        addbutton.clicked.connect(self.add_record)

        # add action
        addaction = self.findChild(QAction)
        addaction.triggered.connect(self.add_record)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_record(self):
        print("add record clicked")


# app = QApplication([])
# window = Dashboard()
# window.location_on_the_screen()
# window.show()
# app.exec_()
