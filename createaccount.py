from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys
from userdataclass import jsondata


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/createaccount.ui", self)
        name = self.findChild(QLineEdit, 'name')
        email = self.findChild(QLineEdit, 'email')
        phone = self.findChild(QLineEdit, 'phone')
        username = self.findChild(QLineEdit, 'username')
        password = self.findChild(QLineEdit, 'password')
        createaccount = self.findChild(QPushButton, 'createacc')
        login = self.findChild(QPushButton, 'login')
        message = self.findChild(QLabel, 'message')

        # define signal for buttons
        createaccount.clicked.connect(self.click_create)
        login.clicked.connect(self.click_login)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def click_create(self):
        # creating dictionary
        info = {
            'name' : self.name.text(),
            'email': self.email.text(),
            'phone': self.phone.text(),
            'username': self.username.text(),
            'pass': self.password.text(),
            'datapath' : ''
        }
        if self.password.text()=='' or self.username.text()=='':
            self.message.setText("You must provide username and password!!")
        else:
            # use jsondata class to store info
            data = jsondata()
            data.writedata(info)

    def click_login(self):
        pass

app = QApplication([])
window = UI()
window.location_on_the_screen()
window.show()
app.exec_()
