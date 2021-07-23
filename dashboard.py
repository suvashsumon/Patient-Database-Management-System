import sqlite3

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5 import *

from addrecord import Addrecord
import sys

from editItem import EditWindow
from makepdf import MakePdf
from userdataclass import jsondata
from viewwork import ViewWindow


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

        # edit button
        self.editbtn = self.findChild(QPushButton, "edit")
        self.editbtn.clicked.connect(self.edit_work)

        # search and filter field
        self.filterField = self.findChild(QLineEdit, "searchField")
        self.filterField.textChanged.connect(self.filter)

        # filter flag
        self.filterFlag = self.findChild(QComboBox, "filterFlag")

        # delete button
        self.deleteButton = self.findChild(QPushButton, "deleteButton")
        self.deleteButton.clicked.connect(self.delete_clicked)

        # view button
        self.viewButton = self.findChild(QPushButton, "viewButton")
        self.viewButton.clicked.connect(self.view_clicked)

        # print button
        self.viewButton = self.findChild(QPushButton, "printButton")
        self.viewButton.clicked.connect(self.print_clicked)

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
            self.tableWidget.setItem(rowindex, 10, QtWidgets.QTableWidgetItem(row[13]))
            self.tableWidget.setItem(rowindex, 11, QtWidgets.QTableWidgetItem(row[11]))
            self.tableWidget.setItem(rowindex, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.tableWidget.setItem(rowindex, 13, QtWidgets.QTableWidgetItem(row[14]))
            self.tableWidget.setItem(rowindex, 14, QtWidgets.QTableWidgetItem(row[15]))
            self.tableWidget.setItem(rowindex, 15, QtWidgets.QTableWidgetItem(row[16]))
            rowindex = rowindex + 1

        conn.commit()
        conn.close()

#  this function is for open edit window to edit selected item
    def edit_work(self):
        selected_id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        self.editwindow = EditWindow(selected_id)
        self.editwindow.location_on_the_screen()
        self.editwindow.show()

#  this function is for open edit window to edit selected item
    def view_clicked(self):
        selected_id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        self.viewwindow = ViewWindow(selected_id)
        self.viewwindow.location_on_the_screen()
        self.viewwindow.show()

# this function is for filter system
    def filter(self):
        flag = self.filterFlag.currentText()
        text = self.filterField.text()
        if len(text) > 1:
            flagRow = 1
            if flag=="ID":
                flagRow = 1
            elif flag=="Name":
                flagRow = 2
            elif flag=="Sex":
                flagRow = 3
            elif flag == "Age":
                flagRow = 4
            elif flag == "Address":
                flagRow = 5
            elif flag == "CC":
                flagRow = 6
            elif flag == "OE":
                flagRow = 7
            elif flag == "RF":
                flagRow = 8
            elif flag == "Path":
                flagRow = 9
            elif flag == "Dxs":
                flagRow = 15
            else:
                flagRow = 16
            datapath = jsondata()
            database = datapath.getdatapath() + "/database.db"
            conn = sqlite3.connect(database)
            sql = "SELECT * FROM entry"
            cur = conn.cursor()
            filterResult = []
            for row in cur.execute(sql):
                if(row[flagRow].lower().find(text.lower()) != -1):
                    filterResult.append(row)

            self.tableWidget.setRowCount(len(filterResult))
            rowindex = 0
            for row in filterResult:
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
                self.tableWidget.setItem(rowindex, 10, QtWidgets.QTableWidgetItem(row[13]))
                self.tableWidget.setItem(rowindex, 11, QtWidgets.QTableWidgetItem(row[11]))
                self.tableWidget.setItem(rowindex, 12, QtWidgets.QTableWidgetItem(row[12]))
                self.tableWidget.setItem(rowindex, 13, QtWidgets.QTableWidgetItem(row[14]))
                self.tableWidget.setItem(rowindex, 14, QtWidgets.QTableWidgetItem(row[15]))
                self.tableWidget.setItem(rowindex, 15, QtWidgets.QTableWidgetItem(row[16]))
                rowindex = rowindex + 1

    # this function is for delete button
    def delete_clicked(self):
        selected_id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        datapath = jsondata()
        database = datapath.getdatapath() + "/database.db"
        conn = sqlite3.connect(database)
        sql = f"DELETE FROM entry WHERE ID={selected_id}"
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Want to delete all data of ID = " + str(selected_id))
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            conn.execute(sql)
        conn.commit()
        conn.close()
        self.refresh_table()

    def print_clicked(self):
        selected_id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        obj = MakePdf(selected_id)
        obj.printwork()
        QMessageBox.about(self, "Success", "Pdf Saved.")


# app = QApplication([])
# window = Dashboard()
# window.location_on_the_screen()
# window.show()
# app.exec_()
