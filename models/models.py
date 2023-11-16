import sqlite3

con = sqlite3.connect("localShopConnectDB.db")
cur = con.cursor()


class User:
    def __init__(self):

        cur.execute("""CREATE TABLE IF NOT EXISTS "user_table" (
        "id"	INTEGER NOT NULL,
        "username"	TEXT NOT NULL UNIQUE,
        "email"	TEXT NOT NULL UNIQUE,
        "phone_number"	INTEGER NOT NULL UNIQUE,
        "shop_name"	TEXT NOT NULL,
        "password"	TEXT NOT NULL,
        "status"	INTEGER NOT NULL DEFAULT 0,
        PRIMARY KEY("id" AUTOINCREMENT)
        )""")

    def register(self, userinfo):
        try:
            cur.execute("""insert into user_table (username,email,phone_number,shop_name,password) values(?,?,?,?,?)""", userinfo)
            con.commit()
        except sqlite3.Error as error:
            return False
        return True

    @staticmethod
    def login(loginInfo):
        try:
            cur.execute("""select id from user_table where email=? and password=?""", loginInfo)
            rows = cur.fetchall()
            if len(rows) < 1:
                cur.execute("""select id from user_table where username=? and password=?""", loginInfo)
                rows = cur.fetchall()
                if len(rows) >= 1:
                    return True
                else:
                    return False

            else:
                return True
        except TypeError as error:
            return False