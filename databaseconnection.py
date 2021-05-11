import sqlite3
from userdataclass import jsondata

class DatabaseConnection:
    def __init__(self):
        self.dataclass = jsondata()
        self.path = self.dataclass.getdatapath()
        self.conn = sqlite3.connect(self.path+'/database.db')
