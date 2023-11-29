from PySide6.QtGui import QStandardItem, QStandardItemModel, Qt
from PySide6.QtWidgets import QLineEdit, QPushButton, QMainWindow, QCompleter, QComboBox
from UI.UI_Manager import UI_Manager
from Themes.Themes import Theme
from configurations.Config import Config
from UI.AddItem import AddItemDialog
from models.models import Product,Bill
from extras.UI_Functionalities import Alert


cnf = Config.getInstance()


class BillItemList:
    items = []
    grandTotalFieldToUpdate = None
    billTable = None

    def __init__(self,totalField,table):
        self.grandTotalFieldToUpdate = totalField
        self.billTable = table


    def addToBill(self,item):
        self.items.append(item)
        return True


    def calculateTotal(self):
        sum = 0
        for row, item in enumerate(self.items):
            total = float(item["Grand Total"])
            sum += total
        self.grandTotalFieldToUpdate.setText(str(sum))

    def clearCart(self):
        self.items = []
        self.billTable.clear()
        headers = ['Item No', "Product Code", 'HSN Code', 'Sale Price', 'Quantity', 'Discount', 'Amount', 'CGST',
                        'SGST', 'IGST', 'Total Tax', 'Grand Total']
        self.billTable.setHorizontalHeaderLabels(headers)
        self.grandTotalFieldToUpdate.setText("")



class DashboardWindow(QMainWindow):
    addNewItemWindow = None  # Instance variable to store AddNewItemWindow instance
    InputFields = {}
    sideNavButtons = {}
    sidenavToggled = False
    product_code_combo = None
    billDB = Bill()
    billItems = None
    bill_ItemNo = 1
    SingleItemInfo = None
    taxRate= None
    headers = []
    def __init__(self):
        #just UI setup part
        super().__init__()
        self.itemInputFields = None
        self.ui = UI_Manager.DashboardUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, Theme.Dashboard)
        cnf.setTheme(self.ui.sideNavigation,Theme.sideNavigation)

        #this part shows the added products
        self.table_view = self.ui.cartView

        #setup initial bill info
        self.ui.itemNo.setText(str(self.bill_ItemNo))

        # Create a model
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)
        self.headers = ['Item No', "Product Code", 'HSN Code', 'Sale Price', 'Quantity', 'Discount', 'Amount', 'CGST', 'SGST', 'IGST','Total Tax','Grand Total']
        self.model.setHorizontalHeaderLabels(self.headers)
        #gathers references to input fields
        self.setupInputFields()
        self.billItems = BillItemList(self.ui.totalAmountCalculated,self.model)



        #sidenavigation configurations
        self.sideNavButtons = self.setupSideNavButtons(self.ui.sideNavigation.children())
        self.sideNavButtons["hamburger"].clicked.connect(self.toggleSideNav)
        self.sideNavButtons['products'].clicked.connect(self.inventoryManager)



        self.product_code_combo = self.ui.ProductCode

        # Connect the completer
        completer = QCompleter(self.product_code_combo.model(), self.product_code_combo)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.product_code_combo.setCompleter(completer)

        self.updateProductCodes()
        self.ui.ProductCode.setCurrentIndex(-1)
        self.ui.ProductCode.currentIndexChanged.connect(self.onceProductCodeSelected)
        self.ui.Quantity.textChanged.connect(self.quantityChanged)
        self.ui.Discount.textChanged.connect(self.discountChanged)
        self.ui.Amount.textChanged.connect(self.amountChanged)

        # setup UI buttons actions
        self.ui.addItemBtn.clicked.connect(self.add_row_to_cart)
        self.ui.cancelBtn.clicked.connect(self.cancel_Item)
        self.ui.cancelBillBtn.clicked.connect(self.cancelBillButtonClicked)




    def cancelBillButtonClicked(self):
        self.billItems.clearCart()

    def onceProductCodeSelected(self):
        if not self.product_code_combo.currentIndex() == -1:
            productCode = self.currentProductCode(self.ui.ProductCode.currentIndex())
            self.setProductInfoFromProductCode(productCode)

    def setProductInfoFromProductCode(self,productCode):
        self.SingleItemInfo = Product.fetchProductDataForBill(productCode)
        self.taxRate = self.SingleItemInfo["taxRate"]

        #update UI elements
        self.InputFields["HSNCode"].setText(str(self.SingleItemInfo['hsnCode']))
        self.InputFields["SalePrice"].setText(str(self.SingleItemInfo['salePrice']))





    def setProductCodes(self, product_codes):
        # Create a custom model for the combo box
        model = QStandardItemModel()
        model.setColumnCount(1)
        model.setRowCount(len(product_codes))

        for row, product in enumerate(product_codes):
            item = QStandardItem(f"{product['productCode']} ({product['productName']})")
            item.setData(product['productCode'], Qt.UserRole)
            model.setItem(row, 0, item)

        # Set the model for the combo box
        self.product_code_combo.setModel(model)

    def currentProductCode(self, index):
        # Handle the selected item (only the product code)
        selected_product_code = self.product_code_combo.currentData(Qt.UserRole)
        #print(f"Selected Product Code: {selected_code}")
        return  selected_product_code

    # Call this function when you want to update the product codes in the combo box
    def updateProductCodes(self):
        product_codes = Product.fetchProductCodes()
        self.setProductCodes(product_codes)


    #add an inventory manager that adds and keeps track of new products:
    def inventoryManager(self):
        if self.addNewItemWindow is None or not self.addNewItemWindow.isVisible():
            self.addNewItemWindow = AddItemDialog()
            self.addNewItemWindow.finished.connect(self.handleAddItemDialogClosed)
            self.addNewItemWindow.show()

    def handleAddItemDialogClosed(self):
        # Slot to handle the closing of the AddItemDialog
        self.addNewItemWindow = None

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
        for field in self.InputFields.values():
            if not field.property("editable"):
                field.setDisabled(True)




    def setComponents(self,dialog):
        self.addStaffWindow = dialog


############################### table data methods ##########################################

    def add_row_to_cart(self):
        #if any field is empty
        for field in self.InputFields.values():
            if field.text() == "" and not field.objectName()=="Discount":
                Alert.show_alert(f"Error: {field.objectName()} is empty")
                return False
        try:
            billItem = self.get_table_row_data(self.InputFields)
            self.billItems.addToBill(billItem)
            self.billItems.calculateTotal()

        except AttributeError as aE:
            print(aE)
        else:
            current_row_count = self.model.rowCount()
            self.model.insertRow(current_row_count)
            for col, col_data in enumerate(billItem.values()):
                item = QStandardItem(col_data)
                self.model.setItem(current_row_count, col, item)
            self.bill_ItemNo += 1
            self.ui.itemNo.setText(str(self.bill_ItemNo))

    def cancel_Item(self):

        for field in self.InputFields.values():
            if not isinstance(field,QComboBox):
                field.clear()
        self.ui.ProductCode.setCurrentIndex(-1)
        self.ui.itemNo.setText(str(self.bill_ItemNo))



    def getDataFromRow(self):
        row_data = self.get_table_row_data(self.InputFields)
        if row_data:
            return row_data
        else:
            print(f"No data found")

    def get_table_row_data(self, inputFields):
        row_data = {key: None for key in self.headers}
        for field in inputFields.values():
            item = field.text()
            column_name = field.placeholderText()
            row_data[column_name] = item
        row_data[self.ui.ProductCode.placeholderText()] = self.currentProductCode(self.ui.ProductCode.currentIndex())
        return row_data


############################### table data methods end ##########################################

############################### input validators ##########################################

    def validateInput(self):
       pass

################################## UI stuff #######################################
    def startMaximised(self):
        self.showMaximized()



###################################################################################
    def quantityChanged(self):
        try:
            quantity = int(self.ui.Quantity.text())
            salePrice = float(self.ui.SalePrice.text())
        except ValueError:
            quantity = 0
            salePrice = 0
        finally:
            amount = quantity * salePrice
            self.ui.Amount.setProperty('originalValue',str(amount))
            self.ui.Amount.setText(str(float(amount)))


    def discountChanged(self):
        if self.ui.Amount.text():
            originalAmount = float(self.ui.Amount.property("originalValue"))
            try:
                discount = float(self.ui.Discount.text())
                newAmount = originalAmount - discount
                self.ui.Amount.setText(str(newAmount))
            except ValueError as err:
                newAmount = originalAmount
                self.ui.Amount.setText(str(newAmount))



    def amountChanged(self):
        if not self.ui.Amount.text():
            return
        try:
            amount = float(self.ui.Amount.text())
            taxes = self.calculate_gst(amount, self.taxRate)
            self.ui.Amount.setText(str(amount))
            self.ui.cgst.setText(str(taxes["CGST"]))
            self.ui.sgst.setText(str(taxes["SGST"]))
            self.ui.igst.setText(str(taxes["IGST"]))
            self.ui.totalTax.setText(str(taxes["GST"]))
            self.ui.grandTotal.setText(str(taxes["grandTotal"]))
        except ValueError as err:
            print(err)



    def performTaxCalculations(self):
        try:
            quantity = int(self.ui.Quantity.text())
        except ValueError:
            quantity = 0
        finally:
            salePrice = float(self.ui.SalePrice.text())
            amount = quantity * salePrice
            taxes = self.calculate_gst(amount, self.taxRate)
            self.ui.Amount.setText(str(amount))
            self.ui.cgst.setText(str(taxes["CGST"]))
            self.ui.sgst.setText(str(taxes["SGST"]))
            self.ui.igst.setText(str(taxes["IGST"]))
            self.ui.totalTax.setText(str(taxes["GST"]))
            self.ui.grandTotal.setText(str(taxes["grandTotal"]))





    def calculate_gst(self, price, gst_percentage):
        # Calculate CGST and SGST
        cgst_sgst_rate = gst_percentage / 2
        cgst_amount = round(price * (cgst_sgst_rate / 100), 2)
        sgst_amount = round(price * (cgst_sgst_rate / 100), 2)

        # Calculate IGST
        igst_rate = gst_percentage
        igst_amount = round(price * (igst_rate / 100), 2)

        totalTax = cgst_amount+sgst_amount+igst_amount
        grandTotal = round(price + totalTax, 2)

        return {
            'CGST': cgst_amount,
            'SGST': sgst_amount,
            'IGST': igst_amount,
            'GST' : totalTax,
            'grandTotal': grandTotal
        }

