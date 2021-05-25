from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit


class EditWindow(QWidget):
    def __init__(self, ids):
        super().__init__()
        uic.loadUi("ui/editrecord.ui", self)

        # id setting
        self.id = self.findChild(QLineEdit, "id")
        self.id.setText(str(ids))

    def location_on_the_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# app = QApplication([])
# window = EditWindow()
# window.location_on_the_screen()
# window.show()
# app.exec_()