from PyQt5.QtWidgets import *
from PyQt5 import uic
from userdataclass import jsondata
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

        username = self.findChild(QLineEdit, 'username')
        password = self.findChild(QLineEdit, 'password')
        message = self.findChild(QLabel, 'message')
        login = self.findChild(QPushButton, 'login')
        login.clicked.connect(self.clicked_btn)
        createacc = self.findChild(QPushButton, 'createaccount')

    def clicked_btn(self):
        # get data from user
        txtusername = self.username.text()
        txtpass = self.password.text()

        # get data from userdata.json file
        userdata = jsondata()
        info = userdata.getdata()

        if txtusername == info['username'] and txtpass == info['pass']:
            self.message.setText("Done!!")
        else:
            self.message.setText("Incorrect password or username")

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


