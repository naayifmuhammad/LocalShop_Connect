from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QLineEdit, QPushButton
from UI.UI_Manager import UI_Manager
from Themes.Themes import Theme
from configurations.Config import Config
from extras.UI_Functionalities import FrameLessWindow


cnf = Config.getInstance()

class DashboardWindow(FrameLessWindow):
    addStaffWindow = None
    InputFields = {}
    sideNavButtons = {}
    sidenavToggled = False
    def __init__(self):
        #just UI setup part
        super().__init__()
        self.itemInputFields = None
        self.ui = UI_Manager.DashboardUI()
        self.ui.setupUi(self)
        self.makeframeLess(True)
        self.setupTitleBar(self,True)
        cnf.setTheme(self, Theme.Dashboard)




        #this part shows the added products
        self.table_view = self.ui.cartView


        #setup UI buttons actions
        self.ui.addItemBtn.clicked.connect(self.add_row_to_cart)
        self.ui.cancelBtn.clicked.connect(self.cancel_Item)

        # Create a model
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)
        self.model.setHorizontalHeaderLabels(["ItemNo", "Product ID", "HSN Code", "Sale Price", "Qty", "Discount", "Amount"])
        self.setupInputFields()
        self.sideNavButtons = self.setupSideNavButtons(self.ui.sidebar.children())
        self.sideNavButtons["hamburger"].clicked.connect(self.toggleSideNav)




    #get all input fields related to item to later fetch data from it and clear it
    def getFields(self,InputFieldList):
        inputFields = {}
        for field in InputFieldList:
            if isinstance(field,QLineEdit):
                inputFields[field.objectName()] = field
        return inputFields

    def setupSideNavButtons(self,sideNavElements):
        sidenavButtons = {}
        for btn in sideNavElements:
            if isinstance(btn,QPushButton):
                sidenavButtons[btn.objectName()] = btn
        return sidenavButtons

    def toggleSideNav(self):
        self.sidenavToggled = not self.sidenavToggled

        for button in self.sideNavButtons.values():
            if self.sidenavToggled:
                button.setText(button.toolTip())
            else:
                button.setText("")

    def setupInputFields(self):
        # create a dictionary of input field, so it's easier to clear and fetch data from them
        self.InputFields.update(self.getFields(self.ui.ItemDetails.children()))
        self.InputFields.update(self.getFields(self.ui.taxDetails.children()))
        #now make sure to set the non editable fields that way:
        nonEditableFields = ['itemNo', 'HSNCode','SalePrice','Amount', 'cgst', 'sgst', 'igst', 'totalTax', 'grandTotal']
        for field in nonEditableFields:
            self.InputFields[field].setDisabled(True)
            self.InputFields[field].setText("Value")

    def setComponents(self,dialog):
        self.addStaffWindow = dialog

############################### table data methods ##########################################

    def add_row_to_cart(self):
        #if any field is empty
        for field in self.InputFields.values():
            if field.text() == "":
                print("Error:", field.objectName() ," is empty")
                return False
        try:
            data = self.get_table_row_data(self.InputFields)
        except AttributeError as aE:
            print(aE)
        else:
            current_row_count = self.model.rowCount()
            self.model.insertRow(current_row_count)
            for col, col_data in enumerate(data.values()):
                item = QStandardItem(col_data)
                self.model.setItem(current_row_count, col, item)

    def cancel_Item(self):
        for field in self.InputFields.values():
            field.clear()



    def getDataFromRow(self):
        row_data = self.get_table_row_data(self.InputFields)

        if row_data:
            return row_data
        else:
            print(f"No data found")

    def get_table_row_data(self, inputFields):
        row_data = {}

        for field in inputFields.values():
            item = field.text()

            column_name = field.objectName()
            row_data[column_name] = item

        return row_data


############################### table data methods end ##########################################

############################### input validators ##########################################

    def validateInput(self):
       pass


############################### table data methods end ##########################################













################################## UI stuff #######################################
    def startMaximised(self):
        self.showMaximized()



if __name__ == "__main__":
    dashboard = DashboardWindow()