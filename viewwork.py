import os
import shutil
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QComboBox, QPlainTextEdit, QPushButton, \
    QListWidget, QFileDialog, QMessageBox

from imageViewer import ImageViewer
from makepdf import MakePdf
from userdataclass import jsondata


class ViewWindow(QWidget):
    def __init__(self, ids):
        super().__init__()
        uic.loadUi("ui/viewrecord.ui", self)

        self.idd = ids

        # id setting
        self.id = self.findChild(QLineEdit, "id")
        self.id.setText(str(ids))
        self.name = self.findChild(QLineEdit, 'name')
        self.age = self.findChild(QLineEdit, 'age')
        self.address = self.findChild(QLineEdit, 'address')
        self.sex = self.findChild(QComboBox, 'sex')
        self.cc = self.findChild(QPlainTextEdit, 'cc')
        self.oe = self.findChild(QPlainTextEdit, 'oe')
        self.rf = self.findChild(QPlainTextEdit, 'rf')
        self.pathreport = self.findChild(QPlainTextEdit, 'pathreport')
        self.viewRediology = self.findChild(QPushButton, 'viewRediology')
        self.listRediology = self.findChild(QListWidget, 'listRadiology')
        self.viewMri = self.findChild(QPushButton, 'viewMri')
        self.listMri = self.findChild(QListWidget, 'listMri')
        self.viewXray = self.findChild(QPushButton, 'viewXray')
        self.listXray = self.findChild(QListWidget, 'listXray')
        self.viewCtscan = self.findChild(QPushButton, 'viewCtscan')
        self.listCtscan = self.findChild(QListWidget, 'listCtscan')
        self.viewPics = self.findChild(QPushButton, 'viewPics')
        self.listPics = self.findChild(QListWidget, 'listPics')
        self.dxs = self.findChild(QPlainTextEdit, 'dxs')
        self.comments = self.findChild(QPlainTextEdit, 'comments')
        self.print = self.findChild(QPushButton, 'print')

        self.loadData(ids)

        # adding signal to the buttons
        self.viewRediology.clicked.connect(self.viewRediology_clicked)
        self.viewMri.clicked.connect(self.viewMri_clicked)
        self.viewCtscan.clicked.connect(self.viewCtscan_clicked)
        self.viewXray.clicked.connect(self.viewXray_clicked)
        self.viewPics.clicked.connect(self.viewPics_clicked)
        self.print.clicked.connect(self.print_clicked)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def viewRediology_clicked(self):
        datapath = jsondata()
        path = datapath.getdatapath() + "/images/"
        images = []
        for x in range(self.listRediology.count()):
            images.append(path+self.listRediology.item(x).text())
        self.imageviewer = ImageViewer(images)
        self.imageviewer.show()

    def viewMri_clicked(self):
        datapath = jsondata()
        path = datapath.getdatapath() + "/images/"
        images = []
        for x in range(self.listMri.count()):
            images.append(path+self.listMri.item(x).text())
        self.imageviewer = ImageViewer(images)
        self.imageviewer.show()

    def viewCtscan_clicked(self):
        datapath = jsondata()
        path = datapath.getdatapath() + "/images/"
        images = []
        for x in range(self.listCtscan.count()):
            images.append(path+self.listCtscan.item(x).text())
        self.imageviewer = ImageViewer(images)
        self.imageviewer.show()

    def viewXray_clicked(self):
        datapath = jsondata()
        path = datapath.getdatapath() + "/images/"
        images = []
        for x in range(self.listXray.count()):
            images.append(path+self.listXray.item(x).text())
        self.imageviewer = ImageViewer(images)
        self.imageviewer.show()

    def viewPics_clicked(self):
        datapath = jsondata()
        path = datapath.getdatapath() + "/images/"
        images = []
        for x in range(self.listPics.count()):
            images.append(path+self.listPics.item(x).text())
        self.imageviewer = ImageViewer(images)
        self.imageviewer.show()

    def loadPics(self, jointpath, flag):
        paths = jointpath.split(',')
        if flag == "radiology":
            for item in paths:
                self.listRediology.addItem(item)
        elif flag == "mri":
            for item in paths:
                self.listMri.addItem(item)
        elif flag == "xray":
            for item in paths:
                self.listXray.addItem(item)
        elif flag == "ctscan":
            for item in paths:
                self.listCtscan.addItem(item)
        elif flag == "pics":
            for item in paths:
                self.listPics.addItem(item)

# this function is for load data from database file
    def loadData(self, id):
        datapath = jsondata()
        database = datapath.getdatapath() + "/database.db"
        conn = sqlite3.connect(database)
        sql = "SELECT * FROM entry WHERE id=" + str(id)
        cur = conn.cursor()
        for row in cur.execute(sql):
            self.name.setText(row[2])
            if row[3] == "male" or row[3] == "Male":
                self.sex.setCurrentText("Male")
            elif row[3] == "female" or row[3] == "Female":
                self.sex.setCurrentText("Female")
            else:
                self.sex.setCurrentText("Others")
            self.age.setText(row[4])
            self.address.setText(row[5])
            self.cc.insertPlainText(row[6])
            self.oe.insertPlainText(row[7])
            self.rf.insertPlainText(row[8])
            self.pathreport.insertPlainText(row[9])
            self.loadPics(row[10], "radiology")
            self.loadPics(row[11], "mri")
            self.loadPics(row[12], "xray")
            self.loadPics(row[13], "ctscan")
            self.loadPics(row[14], "pics")
            self.dxs.insertPlainText(row[15])
            self.comments.insertPlainText(row[16])
        conn.commit()
        conn.close()

#   this function is for save images taken from list, lastly it returns combined files path
    def getImages(self, list, id, flag):
        pass

    def print_clicked(self):
        obj = MakePdf(self.idd)
        obj.printwork()
        QMessageBox.about(self, "Success", "Pdf Saved.")

# app = QApplication([])
# window = EditWindow()
# window.location_on_the_screen()
# window.show()
# app.exec_()