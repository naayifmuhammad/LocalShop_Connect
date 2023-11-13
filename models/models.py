import sqlite3

con = sqlite3.connect("localShopConnectDB.db")
cur = con.cursor()

class Authentication:
    def __init__(self):
        cur.execute('''CREATE TABLE auth(
        username text, 
        password text, 
        )''')
class User:
    def __init__(self):
        cur.execute('''CREATE TABLE users(
        
        )''')

