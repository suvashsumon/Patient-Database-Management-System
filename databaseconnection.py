import sqlite3

class DatabaseConnection:
    def __init__(self):
        conn = sqlite3.connect('test.db')

    def executeQuery(self):
        pass


