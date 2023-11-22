from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from UI.UI_Manager import UI_Manager
from Themes.Themes import Theme
from configurations.Config import Config


cnf = Config.getInstance()

class DashboardWindow(QMainWindow):

    addStaffWindow = None
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.DashboardUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, Theme.Dashboard)
        self.table_view = self.ui.cartView

        self.ui.addItemBtn.clicked.connect(self.add_row_to_cart)

        # Create a model

        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        # Set headers for the columns
        self.model.setHorizontalHeaderLabels(["ItemNo", "Product ID", "HSN Code", "Sale Price", "Qty", "Discount", "Amount"])

    def setComponents(self,dialog):
        self.addStaffWindow = dialog

############################### table data methods ##########################################

    def add_row_to_cart(self):
        current_row_count = self.model.rowCount()
        data = self.get_table_row_data(self.ui.ItemDetails,0)
        print(list(data.values()))
        self.model.insertRow(current_row_count)
        for col, col_data in enumerate(data.values()):
            item = QStandardItem(col_data)
            self.model.setItem(current_row_count, col, item)

    def getDataFromRow(self,rowIndex = 0):
        row_data = self.get_table_row_data(self.ui.ItemDetails, rowIndex)

        if row_data:
            return row_data
        else:
            print(f"No data found for row {rowIndex}")

    def get_table_row_data(self, table_widget, row_index=0):
        row_data = {}

        for col in range(table_widget.columnCount()):
            item = table_widget.item(row_index, col)
            column_name = table_widget.horizontalHeaderItem(col).text()
            row_data[column_name] = item.text()

        return row_data




############################### table data methods end ##########################################

if __name__ == "__main__":
    dashboard = DashboardWindow()