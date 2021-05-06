from PyQt5.QtWidgets import *
from PyQt5 import uic
from userdataclass import jsondata
from dashboard import Dashboard
import sys


class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

        username = self.findChild(QLineEdit, 'username')
        password = self.findChild(QLineEdit, 'password')
        login = self.findChild(QPushButton, 'login')
        login.clicked.connect(self.clicked_login)

    def clicked_login(self):
        # get data from user
        txtusername = self.username.text()
        txtpass = self.password.text()

        # get data from userdata.json file
        userdata = jsondata()
        info = userdata.getdata()

        if txtusername == info['username'] and txtpass == info['pass']:
            self.dashboard = Dashboard()
            self.dashboard.location_on_the_screen()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.about(self, "Error", "Username or password is incorrect.")

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

