import os.path

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

from dashboard import Dashboard
from userdataclass import  jsondata
import sys


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/setting.ui", self)

        # finding chields
        self.setpath = self.findChild(QLineEdit, 'databasepath')
        setpathbtn = self.findChild(QPushButton, 'newpathbtn')
        self.existingpath = self.findChild(QLineEdit, 'existingpath')
        findpathbtn = self.findChild(QPushButton, 'existingpathbtn')
        savesettings = self.findChild(QPushButton, 'save')

        # set signal for this btn
        setpathbtn.clicked.connect(self.setdatabasepath)
        findpathbtn.clicked.connect(self.findexistingpath)
        savesettings.clicked.connect(self.savesettings_func)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setdatabasepath(self):
        folderpath = QFileDialog.getExistingDirectory()
        self.setpath.setText(folderpath)

    def findexistingpath(self):
        folderpath = QFileDialog.getExistingDirectory()
        self.existingpath.setText(folderpath)

    def savesettings_func(self):
        if self.existingpath.text() == '':
            path = self.setpath.text()
            userdata = jsondata()
            userdata.setdatapath(path+'/pdm_database')
            # creating pdm_database folder according to given path
            dirpath = os.path.join(path, 'pdm_database')
            os.mkdir(dirpath)
            dirpath = os.path.join(dirpath, 'images')
            os.mkdir(dirpath)
            # open dashboard
            self.dashboard = Dashboard()
            self.dashboard.location_on_the_screen()
            self.dashboard.show()
            self.close()
        elif self.setpath.text() == '':
            path = self.existingpath.text()
            userdata = jsondata()
            userdata.setdatapath(path)
            self.close()
        elif self.existingpath.text() != '' and self.setpath.text() != '':
            QMessageBox.about(self, "Error", "You must provide only one of them.")

# app = QApplication([])
# window = UI()
# window.location_on_the_screen()
# window.show()
# app.exec_()
