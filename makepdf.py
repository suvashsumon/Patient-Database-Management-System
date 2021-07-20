import sqlite3
from userdataclass import jsondata


class MakePdf:
    def __init__(self, id):
        datapath = jsondata()
        database = datapath.getdatapath() + "/database.db"
        conn = sqlite3.connect(database)
        sql = "SELECT * FROM entry WHERE id=" + str(id)
        cur = conn.cursor()
        self.id = id
        self.name = ''
        for row in cur.execute(sql):
            self.name = row[2]
            if row[3] == "male" or row[3] == "Male":
                self.sex = "Male"
            elif row[3] == "female" or row[3] == "Female":
                self.sex = "Female"
            else:
                self.sex = "Others"
            self.age = row[4]
            self.address = row[5]
            self.cc = row[6]
            self.oe = row[7]
            self.rf = row[8]
            self.pathreport = row[9]
            self.rediology = row[10].split(',')
            self.mri = row[11].split(',')
            self.xray = row[12].split(',')
            self.ctscan = row[13].split(',')
            self.pics = row[14].split(',')
            self.dxs = row[15]
            self.comments = row[16]
        conn.commit()
        conn.close()

    def printwork(self):
        print(self.rediology)



if __name__ == "__main__":
    obj = MakePdf(2013)
    obj.printwork()
