import os
import shutil
import sqlite3

from userdataclass import jsondata
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
import sys

from getId import GetID


class Addrecord(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/addrecord.ui", self)

        # find all input sectors
        self.idtext = GetID() # collect id from database
        self.id = self.findChild(QLineEdit, 'id')
        self.id.setText(self.idtext.getID())
        self.name = self.findChild(QLineEdit, 'name')
        self.age = self.findChild(QLineEdit, 'age')
        self.address = self.findChild(QLineEdit, 'address')
        self.sex = self.findChild(QComboBox, 'sex')
        self.cc = self.findChild(QPlainTextEdit, 'cc')
        self.oe = self.findChild(QPlainTextEdit, 'oe')
        self.rf = self.findChild(QPlainTextEdit, 'rf')
        self.pathreport = self.findChild(QPlainTextEdit, 'pathreport')
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
        self.dxs = self.findChild(QPlainTextEdit, 'dxs')
        self.comments = self.findChild(QPlainTextEdit, 'comments')
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
        # print(filepath[0])
        self.listRediology.addItem(filepath[0])

    def addMri_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        # print(filepath[0])
        self.listMri.addItem(filepath[0])

    def addCtscan_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        # print(filepath[0])
        self.listCtscan.addItem(filepath[0])

    def addXray_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        # print(filepath[0])
        self.listXray.addItem(filepath[0])

    def addPics_clicked(self):
        filepath = QFileDialog.getOpenFileName()
        # print(filepath[0])
        self.listPics.addItem(filepath[0])

    # this function collect list items and joins their text by comma, and finally returns
    def printlist(self, list):
        items = []
        for index in range(list.count()):
            items.append(list.item(index))
        if len(items)>0:
            path = items[0].text()
            for item in range(1, len(items)):
                path = path + ',' + items[item].text()
        else:
            path = ''
        return path

#   this function is for save images taken from list, lastly it returns combined files path
    def savePic(self, list, id, flag):
        items = []
        for index in range(list.count()):
            items.append(list.item(index))
        datapath = jsondata()
        filepath = datapath.getdatapath()
        files = []
        for item in range(0, len(items)):
            split_tup = os.path.splitext(items[item].text())
            file_name = str(id)+"_"+flag+"_"+str(item)+split_tup[1]
            shutil.copy(items[item].text(), filepath+"/images/"+file_name)
            files.append(file_name)
        if len(files)>0:
            path = files[0]
            for i in range(1, len(files)):
                path = path + ',' + files[i]
        else:
            path = ''
        return path

    def addRecord_clicked(self):
        id = self.id.text()
        name = self.name.text()
        sex = self.sex.currentText()
        age = self.age.text()
        address = self.address.text()
        cc = self.cc.toPlainText()
        oe = self.oe.toPlainText()
        rf = self.rf.toPlainText()
        pathreport = self.pathreport.toPlainText()
        radiology = self.printlist(self.listRediology)
        mri = self.printlist(self.listMri)
        ctscan = self.printlist(self.listCtscan)
        xray = self.printlist(self.listXray)
        pics = self.printlist(self.listPics)
        dxs = self.dxs.toPlainText()
        comments = self.comments.toPlainText()

        # saving pics
        self.savePic(self.listRediology,id,"Rediology")
        self.savePic(self.listMri,id,"Mri")
        self.savePic(self.listXray,id,"Xray")
        self.savePic(self.listCtscan,id,"Ctscan")
        self.savePic(self.listPics,id,"Pics")

        # insering data to database
        datapath = jsondata()
        database = datapath.getdatapath()+"/database.db"
        conn = sqlite3.connect(database)
        sql = f"INSERT INTO entry (ID, Name, Sex, Age, Address, CC, OE, RF, Path, Rediology, Mri, Xray, Ctscan, Pics, Dxs, Comments) Values ('{str(id)}', '{name}', '{sex}', '{age}', '{address}', '{cc}', '{oe}', '{rf}', '{pathreport}', '{radiology}', '{mri}','{xray}','{ctscan}','{pics}', '{dxs}', '{comments}')"
        conn.execute(sql)
        conn.commit()
        conn.close()

        # update last id
        updateid = GetID()
        updateid.setID(int(id)+1)

        self.close()

app = QApplication([])
window = Addrecord()
window.location_on_the_screen()
window.show()
app.exec_()
