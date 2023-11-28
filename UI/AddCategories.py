from PySide6.QtWidgets import QMainWindow, QLineEdit
from PySide6.QtCore import Signal
from models.models import Product
from UI.UI_Manager import UI_Manager
from Themes.Themes import Theme
from extras.UI_Functionalities import Alert

from configurations.Config import Config

cnf = Config.getInstance()

class AddCategoriesDialog(QMainWindow):
    InputFields = {}
    info = {}
    finished = Signal()
    updated = Signal()
    productDB = Product()
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.AddCategories()
        self.ui.setupUi(self)
        cnf.setTheme(self, Theme.AddVendor)
        ######################################
        # Setup buttons and stuff
        self.InputFields.update(self.getFields(self.ui.InputFields.children()))
        self.ui.add.clicked.connect(self.attemptToAddCategory)
        self.ui.cancel.clicked.connect(self.cancel)




    def attemptToAddCategory(self):
       try:
           if self.fetchData():
               db_ItemInfo = {
                   'name': self.info["name"],
                   'description': self.info["description"]
               }
               if self.productDB.addCategory(db_ItemInfo):
                   Alert.show_alert(f"Added new category [{self.info['name']}]")
                   self.updated.emit()
               else:
                   Alert.show_alert("Some error occurred, Try again")
       except ValueError as ve:
        Alert.show_alert("Please check your input and try again")


    def fetchData(self):
        #check if any fields are empty
        for field in self.InputFields.values():
            if field.property("mandatory") and field.text() == "":
                Alert.show_alert(f"Error {field.placeholderText()} is empty")
                return False
            else:
                self.info[field.objectName()] = field.text()
        return True



    def cancel(self):
        self.finished.emit()
        self.destroy()

    #get all input fields related to item to later fetch data from it and clear it
    def getFields(self,InputFieldList):
        inputFields = {}
        for field in InputFieldList:
            if isinstance(field,QLineEdit):
                inputFields[field.objectName()] = field
        return inputFields
