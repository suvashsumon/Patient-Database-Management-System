from PyQt5.QtWidgets import *
from PyQt5 import uic
from userdataclass import jsondata
from dashboard import Dashboard
from PyQt5.QtGui import QIcon, QPixmap
import sys


class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/imageviewer.ui", self)

        self.image = self.findChild(QLabel, 'image')

        pixmap = QPixmap('/home/suvashkumar/Desktop/programming/pdm_database/images/2002_Rediology_0.jpg')
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)

app = QApplication([])
window = Login()
window.show()
app.exec_()