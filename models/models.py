import sqlite3
import re
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

    @staticmethod
    def register(userinfo):
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

    @staticmethod
    def usernameExists(username):
        try:
            cur.execute(f"""select id from user_table where username = '{username}'""")
            rows = cur.fetchall()
            if len(rows) >= 1:
                return True
            else:
                return False
        except sqlite3.Error as error:
            print(error)
            return True


    @staticmethod
    def emailExists(email):
        try:
            cur.execute(f"select id from user_table where email='{email}'")
            rows = cur.fetchall()
            if len(rows) >= 1:
                return True
            else:
                return False
        except sqlite3.Error as error:
            return True


    @staticmethod
    def emailValid(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            return True
        else:
            return False

    @staticmethod
    def isNumberValid(number):
        pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
        match = re.search(pattern, number)
        if match:
            return True
        return False



    @staticmethod
    def numberExists(number):
        try:
            cur.execute(f"""select id from user_table where phone_number='{number}'""")
            rows = cur.fetchall()
            if len(rows) >= 1:
                return True
            else:
                return False
        except sqlite3.Error as error:
            return True

class Product:
    def __init__(self):

        try:
            cur.execute("""CREATE TABLE IF NOT EXISTS "categories" (
            "id"	INTEGER NOT NULL,
            "name"	TEXT NOT NULL UNIQUE,
            "description"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
            );""")

            cur.execute("""CREATE TABLE IF NOT EXISTS "vendors" (
        	"id"	INTEGER NOT NULL,
        	"shopName"	TEXT NOT NULL UNIQUE,
        	"ownerName"	TEXT,
        	"location"	TEXT,
        	PRIMARY KEY("id" AUTOINCREMENT)
            );""")

            cur.execute("""CREATE TABLE IF NOT EXISTS "products" (
        	"id"	INTEGER NOT NULL,
        	"productCode"	TEXT NOT NULL UNIQUE,
        	"productName"	TEXT NOT NULL UNIQUE,
        	"vendorID"	TEXT NOT NULL,
        	"categoryID"	TEXT NOT NULL,
        	"costPrice"	REAL NOT NULL,
        	"salePrice"	REAL NOT NULL,
        	"hsnCode"	INTEGER,
        	"taxRate"	INTEGER NOT NULL,
        	"qtyInStock"	INTEGER NOT NULL DEFAULT 0,
        	"minStockLevel"	INTEGER NOT NULL DEFAULT 0,
        	FOREIGN KEY("vendorID") REFERENCES "vendors"("shopName"),
        	FOREIGN KEY("categoryID") REFERENCES "categories"("name"),
        	PRIMARY KEY("id" AUTOINCREMENT)
            )""")
        except sqlite3.Error as error:
            print(error)

    @staticmethod
    def addProduct(prodInfo):
        try:
            # Insert data into the "products" table
            cur.execute("""
                INSERT INTO "main"."products" ("productCode", "productName", "vendorID", "categoryID", "costPrice", "salePrice", "hsnCode", "taxRate", "qtyInStock", "minStockLevel") 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                prodInfo["productCode"],
                prodInfo["productName"],
                prodInfo["vendorID"],
                prodInfo["categoryID"],
                prodInfo["costPrice"],
                prodInfo["salePrice"],
                prodInfo["hsnCode"],
                prodInfo["taxRate"],
                prodInfo["qtyInStock"],
                prodInfo["minStockLevel"]
            ))

            # Commit the transaction
            con.commit()

        except sqlite3.Error as error:
            return False
        return True\

    @staticmethod
    def addVendor(vendorInfo):
        try:
            # Insert data into the "products" table
            cur.execute("""
                INSERT INTO "main"."vendors" ("shopName", "ownerName","location") VALUES (?, ?, ?);
            """, (
                vendorInfo["shopName"],
                vendorInfo["ownerName"],
                vendorInfo["location"],
            ))

            # Commit the transaction
            con.commit()

        except sqlite3.Error as error:
            print(error)
            return False
        return True

    @staticmethod
    def addCategory(categoryInfo):
        try:
            # Insert data into the "products" table
            cur.execute("""
                INSERT INTO "main"."categories" ("name", "description") VALUES (?, ?);
            """, (
                categoryInfo["name"],
                categoryInfo["description"],
            ))

            # Commit the transaction
            con.commit()

        except sqlite3.Error as error:
            return False
        return True

    @staticmethod
    def fetchCategories():
        cur.execute("""SELECT name FROM categories;""")
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append(row[0])
        return data
    @staticmethod
    def fetchVendors():
        cur.execute("""SELECT shopName FROM vendors;""")
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append(row[0])
        return data

    @staticmethod
    def fetchProductCodes():
        cur.execute("""SELECT productCode, productName from products;""")
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append({'productCode':row[0],'productName':row[1]})
        return data


    @staticmethod
    def fetchProductDataForBill(productCode):
        try:
            cur.execute("""SELECT hsnCode, salePrice, taxRate FROM products WHERE productCode = ?;""",(productCode,))
            row = cur.fetchone()
            productDataForBill = {"hsnCode": row[0], "salePrice": row[1], "taxRate": row[2]}

            return productDataForBill

        except sqlite3.Error as err:
            print(err)


class Order:
    def __init__(self):
        cur.execute("""CREATE TABLE IF NOT EXISTS order_log (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
        );""")

        cur.execute("""CREATE TABLE IF NOT EXISTS sales_log (
        sl_no INTEGER PRIMARY KEY,
        orderNo INTEGER REFERENCES order_log(order_id),
        productCode TEXT,
        quantity INTEGER,
        discount REAL); """)



    @staticmethod
    def placeOrder(cartItems):
        print("this is the cart items list that I am sending: ",cartItems)
        try:
            cur.execute("""INSERT INTO order_log (date_time) VALUES (CURRENT_TIMESTAMP);""")
            con.commit()
            cur.execute("""SELECT max(order_id) AS order_id from order_log""")
            res = cur.fetchone()
            order_id = res[0]
            if order_id is None:
                return False

            #now for inserting the cart items for the particular order:
            for item in cartItems:
                insert_query = """
                                INSERT INTO sales_log (orderNo, productCode, quantity, discount)
                                VALUES (?, ?, ?, ?)
                            """
                cur.execute(insert_query, (
                    order_id,
                    item['product_code'],
                    item['quantity'],
                    item['discount']
                ))
            con.commit()

        except sqlite3.Error as error:
            print(error)
            return False, error
        return True

