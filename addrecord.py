from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys


class Addrecord(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/addrecord.ui", self)

        # find all input sectors
        self.id = self.findChild(QLineEdit, 'id')
        self.name = self.findChild(QLineEdit, 'name')
        self.age = self.findChild(QLineEdit, 'age')
        self.address = self.findChild(QLineEdit, 'address')
        self.sex = self.findChild(QComboBox, 'sex')
        self.cd = self.findChild(QTextEdit, 'cc')
        self.oe = self.findChild(QTextEdit, 'oe')
        self.rf = self.findChild(QTextEdit, 'rf')
        self.pathreport = self.findChild(QTextEdit, 'pathreport')
        self.addRediology = self.findChild(QPushButton, 'addRediology')
        self.listRediology = self.findChild(QListWidget, 'listRadiology')
        self.addMri = self.findChild(QPushButton, 'addMri')
        self.listMri = self.findChild(QListWidget, 'listMri')
        self.addXray = self.findChild(QPushButton, 'addXray')
        self.listXray = self.findChild(QListWidget, 'listXray')
        self.addCtscan = self.findChild(QPushButton, 'addCtscan')
        self.listCtscan = self.findChild(QListWidget, 'listCtscan')
        self.addPics = self.findChild(QPushButton, 'addPics')
        self.listPics = self.findChild(QListWidget, 'listPics')
        self.dxs = self.findChild(QTextEdit, 'dxs')
        self.comments = self.findChild(QTextEdit, 'comments')
        self.addRecord = self.findChild(QPushButton, 'addrecord')

        # adding signal to the buttons
        self.addRediology.clicked.connect(self.addRediology_clicked)
        self.addMri.clicked.connect(self.addMri_clicked)
        self.addCtscan.clicked.connect(self.addCtscan_clicked)
        self.addXray.clicked.connect(self.addXray_clicked)
        self.addPics.clicked.connect(self.addPics_clicked)
        self.addRecord.clicked.connect(self.addRecord_clicked)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addRediology_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        print(filepath[0])
        self.listRediology.addItem(filepath[0])

    def addMri_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        print(filepath[0])
        self.listMri.addItem(filepath[0])

    def addCtscan_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        print(filepath[0])
        self.listCtscan.addItem(filepath[0])

    def addXray_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        print(filepath[0])
        self.listXray.addItem(filepath[0])

    def addPics_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        print(filepath[0])
        self.listPics.addItem(filepath[0])

    def addRecord_clicked(self):
        pass

app = QApplication([])
window = Addrecord()
window.location_on_the_screen()
window.show()
app.exec_()
