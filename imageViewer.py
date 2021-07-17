from PyQt5.QtWidgets import *
from PyQt5 import uic
from userdataclass import jsondata
from PyQt5.QtGui import QIcon, QPixmap
import sys


class ImageViewer(QWidget):
    def __init__(self, images):
        super().__init__()
        uic.loadUi("ui/imageViewer.ui", self)

        self.images = images

        self.imagefield = self.findChild(QLabel, 'image')
        self.previousBtn = self.findChild(QPushButton, 'previousImage')
        self.nextBtn = self.findChild(QPushButton, 'nextImage')
        self.imageCounter = self.findChild(QLabel, 'imageCounter')

        self.previousBtn.clicked.connect(self.loadPreviousImage)
        self.nextBtn.clicked.connect(self.loadNextImage)

        self.counter = 0
        self.total = len(self.images)
        self.pixmap = QPixmap(self.images[self.counter])
        self.imagefield.setPixmap(self.pixmap)
        self.imagefield.setScaledContents(True)
        self.imageCounter.setText(str(self.counter+1) + "/" + str(self.total))


    def loadPreviousImage(self):
        self.counter -= 1
        if self.counter < 0:
            self.counter = self.total - 1
        self.pixmap = QPixmap(self.images[self.counter])
        self.imagefield.setPixmap(self.pixmap)
        self.imageCounter.setText(str(self.counter+1) + "/" + str(self.total))

    def loadNextImage(self):
        self.counter += 1
        if self.counter > self.total - 1:
            self.counter = 0
        self.pixmap = QPixmap(self.images[self.counter])
        self.imagefield.setPixmap(self.pixmap)
        self.imageCounter.setText(str(self.counter+1) + "/" + str(self.total))

# app = QApplication([])
# images = [
#     "/home/suvashkumar/Desktop/programming/pdm_database/images/3505_Mri_0.jpg",
#     "/home/suvashkumar/Desktop/programming/pdm_database/images/3508_Pics_0.jpg",
#     "/home/suvashkumar/Desktop/programming/pdm_database/images/hello.png",
#     "/home/suvashkumar/Desktop/programming/pdm_database/images/3508_Mri_0.png"
# ]
# window = ImageViewer(images)
# window.show()
# app.exec_()