from PyQt5.QtWidgets import QApplication
import login


app = QApplication([])
window = login.UI()
window.show()
app.exec_()