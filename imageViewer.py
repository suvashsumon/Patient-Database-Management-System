from PyQt5.QtWidgets import *
from PyQt5 import uic
from userdataclass import jsondata
from dashboard import Dashboard
from PyQt5.QtGui import QIcon, QPixmap
import sys


class Login(QWidget):
    def __init__(self, images):
        super().__init__()
        uic.loadUi("ui/imageViewer.ui", self)

        self.image = self.findChild(QLabel, 'image')
        self.previousBtn = self.findChild(QPushButton, 'previousImage')
        self.nextBtn = self.findChild(QPushButton, 'nextImage')
        self.imageCounter = self.findChild(QLabel, 'imageCounter')

        self.previousBtn.clicked.connect(self.previousImage)
        self.nextBtn.clicked.connect(self.nextImage)

        self.counter = 0
        self.total = len(images)
        self.pixmap = QPixmap(self.images[self.counter])
        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)


    def previousImage(self):
        self.counter -= 1
        if self.counter < 0:
            self.counter = self.total - 1
        self.pixmap = QPixmap(self.images[self.counter])
        self.image.setPixmap(self.pixmap)

    def nextImage(self):
        self.counter += 1
        if self.counter > self.total - 1:
            self.counter = 0
        self.pixmap = QPixmap(self.images[self.counter])
        self.image.setPixmap(self.pixmap)

app = QApplication([])
window = Login()
window.show()
app.exec_()