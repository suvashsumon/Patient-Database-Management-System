import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QComboBox, QPlainTextEdit, QPushButton, \
    QListWidget

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
        self.addRecord = self.findChild(QPushButton, 'savechanges')

        self.loadData(ids)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
            self.loadPics(row[12], "ctscan")
            self.loadPics(row[13], "xray")
            self.loadPics(row[14], "pics")
            self.dxs.insertPlainText(row[15])
            self.comments.insertPlainText(row[16])
        conn.commit()
        conn.close()


# app = QApplication([])
# window = EditWindow()
# window.location_on_the_screen()
# window.show()
# app.exec_()