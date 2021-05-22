import sqlite3

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5 import *
from addrecord import Addrecord
import sys

from userdataclass import jsondata


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dashboard.ui", self)

        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.refresh_table()

        # add button
        self.addbutton = self.findChild(QPushButton, 'addrecord')
        self.addbutton.clicked.connect(self.add_record)

        # add action
        self.addaction = self.findChild(QAction)
        self.addaction.triggered.connect(self.add_record)

        # refresh button
        self.refresh = self.findChild(QPushButton, "refresh")
        self.refresh.clicked.connect(self.refresh_table)

        # refresh action
        self.refreshaction = self.findChild(QAction, "actionRefresh")
        self.refreshaction.triggered.connect(self.refresh_table)

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_record(self):
        self.window = Addrecord()
        self.window.location_on_the_screen()
        self.window.show()

    def refresh_table(self):
        datapath = jsondata()
        database = datapath.getdatapath() + "/database.db"
        conn = sqlite3.connect(database)
        sql = "SELECT * FROM entry"
        cur = conn.cursor()
        result = cur.execute(sql)
        no_row = len(result.fetchall())

        self.tableWidget.setRowCount(no_row)
        rowindex = 0
        for row in cur.execute(sql):
            self.tableWidget.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(rowindex, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(rowindex, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(rowindex, 4, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(rowindex, 5, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(rowindex, 6, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(rowindex, 7, QtWidgets.QTableWidgetItem(row[8]))
            self.tableWidget.setItem(rowindex, 8, QtWidgets.QTableWidgetItem(row[9]))
            self.tableWidget.setItem(rowindex, 9, QtWidgets.QTableWidgetItem(row[10]))
            self.tableWidget.setItem(rowindex, 10, QtWidgets.QTableWidgetItem(row[11]))
            self.tableWidget.setItem(rowindex, 11, QtWidgets.QTableWidgetItem(row[12]))
            self.tableWidget.setItem(rowindex, 12, QtWidgets.QTableWidgetItem(row[13]))
            self.tableWidget.setItem(rowindex, 13, QtWidgets.QTableWidgetItem(row[14]))
            self.tableWidget.setItem(rowindex, 14, QtWidgets.QTableWidgetItem(row[15]))
            rowindex = rowindex + 1

        conn.commit()
        conn.close()



# app = QApplication([])
# window = Dashboard()
# window.location_on_the_screen()
# window.show()
# app.exec_()
