from PyQt5.QtWidgets import QApplication

from createaccount import Createaccount
import login
import userdataclass

userdata = userdataclass.jsondata()
info = userdata.getdata()
app = QApplication([])
if info['username'] == '' or info['pass']=='':
    window = Createaccount()
    window.location_on_the_screen()
    window.show()
else:
    window = login.Login()
    window.location_on_the_screen()
    window.show()
app.exec_()