from models import db_connection


class Shop:
    def __init__(self, data_to_insert):
        self.shop_data = {
            'shop_name': data_to_insert['shop_name'],
            'password': data_to_insert['password'],
            'geolocation': data_to_insert['geolocation'],
            'phone_number': data_to_insert['phone_number'],
            'email': data_to_insert['email'],
            'owner_name': data_to_insert['owner_name'],
        }

    def add_new_shop(self):
        try:
            # Connect to the database
            connection = db_connection.serverDB.connect()

            if connection is not None:
                # Create a cursor object to execute SQL queries
                cursor = connection.cursor(prepared=True)

                insert_query = """
                    INSERT INTO shop_information (
                        shop_name, password, geolocation, phone_number, email,
                        owner_name
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """

                # Execute the query with data from the self.shop_data dictionary
                cursor.execute(insert_query, (
                    self.shop_data['shop_name'],
                    self.shop_data['password'],
                    self.shop_data['geolocation'],
                    self.shop_data['phone_number'],
                    self.shop_data['email'],
                    self.shop_data['owner_name']
                ))

                # Commit the changes to the database
                connection.commit()

                print('Data inserted successfully')

        except Exception as e:
            print(f'Error: {e}')

        finally:
            # Close the cursor and disconnect from the database in a finally block
            if 'cursor' in locals() and cursor is not None:
                try:
                    cursor.close()
                except AttributeError:
                    pass  # CMySQLCursorPrepared object has no attribute 'close'

            db_connection.serverDB.disconnect(connection)

class SyncProducts:
    def __init__(self):
        pass

    def start_product_synchronisation(self, product_details_to_sync):
        try:
            # Connect to the database
            connection = db_connection.serverDB.connect()

            if connection is not None:
                # Create a cursor object to execute SQL queries
                cursor = connection.cursor(prepared=True)

                # Assuming product_details_to_sync is a dictionary with the necessary values
                insert_query = """
                    INSERT INTO product_catalog (
                        product_id, product_code, product_name, product_price, hsn_code, product_quantity_in_stock
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """

                # Extract values from the dictionary
                values_to_insert = (
                    product_details_to_sync['product_id'],
                    product_details_to_sync['product_code'],
                    product_details_to_sync['product_name'],
                    product_details_to_sync['product_price'],
                    product_details_to_sync['hsn_code'],
                    product_details_to_sync['product_quantity_in_stock']
                )

                # Execute the query with values from the dictionary
                cursor.execute(insert_query, values_to_insert)

                # Commit the changes to the database
                connection.commit()

                print('Data inserted successfully')
                return True

        except Exception as e:
            print(f'Error: {e}')
            db_connection.serverDB.disconnect(connection)
            return False

        finally:
            # Close the cursor and disconnect from the database in a finally block
            if 'cursor' in locals() and cursor is not None:
                try:
                    cursor.close()
                except AttributeError:
                    pass  # CMySQLCursorPrepared object has no attribute 'close'

            db_connection.serverDB.disconnect(connection)

