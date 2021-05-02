from PyQt5.QtWidgets import QApplication
import login


app = QApplication([])
window = login.UI()
window.location_on_the_screen()
window.show()
app.exec_()