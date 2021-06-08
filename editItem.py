import os
import shutil
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QComboBox, QPlainTextEdit, QPushButton, \
    QListWidget, QFileDialog

from userdataclass import jsondata


class EditWindow(QWidget):
    def __init__(self, ids):
        super().__init__()
        uic.loadUi("ui/editrecord.ui", self)

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
        self.saveChanges = self.findChild(QPushButton, 'savechanges')

        self.loadData(ids)

        # adding signal to the buttons
        self.addRediology.clicked.connect(self.addRediology_clicked)
        self.addMri.clicked.connect(self.addMri_clicked)
        self.addCtscan.clicked.connect(self.addCtscan_clicked)
        self.addXray.clicked.connect(self.addXray_clicked)
        self.addPics.clicked.connect(self.addPics_clicked)
        self.saveChanges.clicked.connect(self.saveChanges_clicked)

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
    def savePic(self, list, id, flag):
        items = []
        for index in range(list.count()):
            if list.item(index).text() != '':
                items.append(list.item(index))
        datapath = jsondata()
        filepath = datapath.getdatapath()
        files = []
        for item in range(0, len(items)):
            split_tup = os.path.splitext(items[item].text())
            file_name = str(id)+"_"+flag+"_"+str(item)+split_tup[1]
            if len(items[item].text().split("/"))>1:  #just checking that if file already exitst in database or not
                shutil.copy(items[item].text(), filepath+"/images/"+file_name)
            files.append(file_name)
        if len(files)>0:
            path = files[0]
            for i in range(1, len(files)):
                path = path + ',' + files[i]
        else:
            path = ''
        return path

    def saveChanges_clicked(self):
        id = self.id.text()
        name = self.name.text()
        sex = self.sex.currentText()
        age = self.age.text()
        address = self.address.text()
        cc = self.cc.toPlainText()
        oe = self.oe.toPlainText()
        rf = self.rf.toPlainText()
        pathreport = self.pathreport.toPlainText()
        # radiology = self.printlist(self.listRediology)
        # mri = self.printlist(self.listMri)
        # ctscan = self.printlist(self.listCtscan)
        # xray = self.printlist(self.listXray)
        # pics = self.printlist(self.listPics)
        dxs = self.dxs.toPlainText()
        comments = self.comments.toPlainText()

        # saving pics
        radiology = self.savePic(self.listRediology,id,"Rediology")
        mri = self.savePic(self.listMri,id,"Mri")
        xray = self.savePic(self.listXray,id,"Xray")
        ctscan = self.savePic(self.listCtscan,id,"Ctscan")
        pics = self.savePic(self.listPics,id,"Pics")

        # insering data to database
        datapath = jsondata()
        database = datapath.getdatapath()+"/database.db"
        conn = sqlite3.connect(database)
        sql = f"UPDATE entry SET Name='{name}', Sex='{sex}', Age='{age}', Address='{address}', CC='{cc}', OE='{oe}', RF='{rf}', Path='{pathreport}', Rediology='{radiology}', Mri='{mri}', Xray='{xray}', Ctscan='{ctscan}', Pics='{pics}', Dxs='{dxs}', Comments='{comments}' WHERE ID='{str(id)}'"
        conn.execute(sql)
        conn.commit()
        conn.close()

        self.close()

# app = QApplication([])
# window = EditWindow()
# window.location_on_the_screen()
# window.show()
# app.exec_()