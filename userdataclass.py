import json

class jsondata:
    # user database file location
    datafile = "data/userdata.json"

    def writedata(self, dictionary):
        with open(self.datafile, "w") as datafile:
            json.dump(dictionary, datafile)


    def getdata(self):
        with open(self.datafile, "r") as datafile:
            data = json.load(datafile)
        return data

    def getdatapath(self):
        with open(self.datafile, "r") as datafile:
            data = json.load(datafile)
        return data['datapath']

    def setdatapath(self, path):
        with open(self.datafile, "r") as datafile:
            data = json.load(datafile)
        data['datapath'] = path
        with open(self.datafile, "w") as datafile:
            json.dump(data, datafile)