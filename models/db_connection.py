import mysql.connector

class serverDB:
    @staticmethod
    def connect():
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                port=3307,
                database='localshop_connect_db'
            )

            if connection.is_connected():
                print('Connected to MySQL database')

            return connection

        except mysql.connector.Error as e:
            print(f'Error: {e}')
            return None

    @staticmethod
    def disconnect(connection):
        try:
            if connection is not None and connection.is_connected():
                connection.close()
                print('Connection closed')
        except mysql.connector.Error as err:
            print(err)
