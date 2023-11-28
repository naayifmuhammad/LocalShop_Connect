from PySide6.QtWidgets import QMainWindow, QLineEdit, QComboBox
from PySide6.QtCore import Signal
from models.models import Product
from UI.UI_Manager import UI_Manager
from Themes.Themes import Theme
from extras.UI_Functionalities import Alert
from UI.AddVendor import AddVendorDialog
from UI.AddCategories import AddCategoriesDialog

from configurations.Config import Config

cnf = Config.getInstance()

class AddItemDialog(QMainWindow):
    InputFields = {}
    productInfo = {}
    addVendorWindow = None
    addCategoryWindow = None
    finished = Signal()
    productDB = Product()
    comboBox_vendors_data = None
    comboBox_categories_data = None


    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.AddItemUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, Theme.AddProduct)
        ######################################
        # Setup buttons and stuff
        self.InputFields.update(self.getFields(self.ui.ItemInfoFrame1.children()))
        self.InputFields.update(self.getFields(self.ui.ItemInfoFrame2.children()))
        self.ui.addItem.clicked.connect(self.attemptToAddProduct)
        self.ui.cancelItem.clicked.connect(self.cancelItem)
        self.ui.actionAdd_Vendors.triggered.connect(self.openAddNewVendor)
        self.ui.actionAdd_Categories.triggered.connect(self.openAddNewCategory)
        self.ui.productCategory.addItems(self.productDB.fetchCategories())
        self.ui.vendor.addItems(self.productDB.fetchVendors())





    def updateDropDownData(self):
        self.ui.productCategory.clear()
        self.ui.vendor.clear()
        self.ui.productCategory.addItems(self.productDB.fetchCategories())
        self.ui.vendor.addItems(self.productDB.fetchVendors())
        try:
            self.addVendorWindow.updated.disconnect()
            self.addCategoryWindow.updated.disconnect()
        except AttributeError:
            pass


    def attemptToAddProduct(self):
       try:
           if self.addNewProduct():
               db_ItemInfo = {
                   'productCode': self.productInfo["productCode"],
                   'productName': self.productInfo["productName"],
                   'vendorID': str(self.productInfo["vendor"]),
                   'categoryID': str(self.productInfo["productCategory"]),
                   'costPrice': float(self.productInfo["costPrice"]),
                   'salePrice': float(self.productInfo["salePrice"]),
                   'hsnCode': int(self.productInfo["hsnCode"]),
                   'taxRate': int(self.productInfo["taxRate"]),
                   'qtyInStock': int(self.productInfo["qtyInStock"]),
                   'minStockLevel': int(self.productInfo["minStockLevel"])
               }
               if self.productDB.addProduct(db_ItemInfo):
                   print("Product successfully added")
                   Alert.show_alert("Product successfully added to database")
                   self.clear_input_fields()

               else:
                   Alert.show_alert("Some error occurred, Try again")
       except ValueError as ve:
        Alert.show_alert("Please check your input and try again")

    def clear_input_fields(self):
        for field in self.InputFields.values():
            if isinstance(field, QLineEdit):
                field.setText("")
            if isinstance(field, QComboBox):
                field.clear()


    def addNewProduct(self):
        #check if any fields are empty
        for field in self.InputFields.values():
            if field.property("mandatory"):
                if isinstance(field,QLineEdit) and field.text()=="":
                    Alert.show_alert(f"Error {field.placeholderText()} is empty")
                    return False

                if isinstance(field,QComboBox) and field.currentText()=="":
                    Alert.show_alert(f"Choose a {field.placeholderText()}")
                    return False
                self.productInfo[field.objectName()] = field.text() if isinstance(field, QLineEdit) else field.currentText()
            else:
                self.productInfo[field.objectName()] = field.text() if isinstance(field, QLineEdit) else field.currentText()
        return True



    def cancelItem(self):
        self.finished.emit()
        self.destroy()

    #get all input fields related to item to later fetch data from it and clear it
    def getFields(self,InputFieldList):
        inputFields = {}
        for field in InputFieldList:
            if isinstance(field,QLineEdit) or isinstance(field,QComboBox):
                inputFields[field.objectName()] = field
        return inputFields

    def openAddNewCategory(self):
        if self.addCategoryWindow is None or not self.addCategoryWindow.isVisible():
            self.addCategoryWindow = AddCategoriesDialog()
            self.addCategoryWindow.updated.connect(self.updateDropDownData)
            self.addCategoryWindow.finished.connect(self.handleAddCategoryWindowClosed)
            self.addCategoryWindow.show()

    def handleAddCategoryWindowClosed(self):
        # Slot to handle the closing
        self.addCategoryWindow = None


    #add an inventory manager that adds and keeps track of new products:
    def openAddNewVendor(self):
        if self.addVendorWindow is None or not self.addVendorWindow.isVisible():
            self.addVendorWindow = AddVendorDialog()
            self.addVendorWindow.updated.connect(self.updateDropDownData)
            self.addVendorWindow.finished.connect(self.handleAddItemDialogClosed)
            self.addVendorWindow.show()

    def handleAddItemDialogClosed(self):
        # Slot to handle the closing
        self.addVendorWindow = None