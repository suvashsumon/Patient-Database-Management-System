from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)

        username = self.findChild(QTextEdit, 'username')
        password = self.findChild(QTextEdit, 'password')
        login = self.findChild(QPushButton, 'login')
        login.clicked.connect(self.clicked_btn)
        createacc = self.findChild(QPushButton, 'createaccount')

    def clicked_btn(self):
        txtusername = self.username.text()
        txtpass = self.password.text()
        if txtusername == "suvashkumar" and txtpass == "0055":
            print("Hello world")
        else:
            print("Sorry username or password is incorrect.")

    def location_on_the_screen(self):
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


