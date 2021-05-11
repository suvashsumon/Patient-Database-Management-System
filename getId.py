import sqlite3
from userdataclass import jsondata


class GetID:
    def __init__(self):
        self.dataclass = jsondata()
        self.path = self.dataclass.getdatapath()

    def getID(self):
        conn = sqlite3.connect(self.path + '/database.db')
        cursor = conn.execute("SELECT currentId FROM config;")
        for row in cursor:
            id = row[0]
        conn.close()
        return id

    def setID(self, id):
        conn = sqlite3.connect(self.path + '/database.db')
        sql = "UPDATE config set currentId = " + str(id) +";"
        conn.execute(sql)
        conn.commit()
        conn.close()


# test = GetID()
# test.setID(2001)
# print(test.getID())