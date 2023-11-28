import unittest
from models.models import User, Product, Bill

class TestUser(unittest.TestCase):

    def test_register_user(self):
        user_info = ("testuser", "testemail@example.com", "1234567890", "testshop", "testpassword")
        self.assertTrue(User.register(user_info))

    def test_login_user(self):
        login_info = ("testemail@example.com", "testpassword")
        self.assertTrue(User.login(login_info))

    def test_username_exists(self):
        self.assertTrue(User.usernameExists("testuser"))

    def test_email_exists(self):
        self.assertTrue(User.emailExists("testemail@example.com"))

    def test_email_valid(self):
        self.assertTrue(User.emailValid("testemail@example.com"))
        self.assertFalse(User.emailValid("invalidemail"))

    def test_number_exists(self):
        self.assertTrue(User.numberExists("1234567890"))

    def test_is_number_valid(self):
        self.assertTrue(User.isNumberValid("1234567890"))
        self.assertFalse(User.isNumberValid("invalidnumber"))


class TestProduct(unittest.TestCase):

    def test_add_product(self):
        product_info = {
            "productCode": "testcode",
            "productName": "testproduct",
            "vendorID": "testvendor",
            "categoryID": "testcategory",
            "costPrice": 10.0,
            "salePrice": 20.0,
            "hsnCode": 123,
            "taxRate": 5,
            "qtyInStock": 50,
            "minStockLevel": 10
        }
        self.assertTrue(Product.addProduct(product_info))

    def test_add_vendor(self):
        vendor_info = {
            "shopName": "testshop",
            "ownerName": "testowner",
            "location": "testlocation"
        }
        self.assertTrue(Product.addVendor(vendor_info))

    def test_add_category(self):
        category_info = {
            "name": "testcategory",
            "description": "testdescription"
        }
        self.assertTrue(Product.addCategory(category_info))

    def test_fetch_categories(self):
        categories = Product.fetchCategories()
        self.assertTrue(isinstance(categories, list))

    def test_fetch_vendors(self):
        vendors = Product.fetchVendors()
        self.assertTrue(isinstance(vendors, list))

    def test_fetch_product_codes(self):
        product_codes = Product.fetchProductCodes()
        self.assertTrue(isinstance(product_codes, list))


class TestBill(unittest.TestCase):

    def test_get_bill_no(self):
        bill = Bill()
        bill_no = bill.getBillNo()
        self.assertTrue(isinstance(bill_no, int))

if __name__ == '__main__':
    unittest.main()
