from PySide6.QtWidgets import QMainWindow
from UI.UI_Manager import UI_Manager
from configurations.Config import Config


cnf = Config.getInstance()

class DashboardWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.DashboardUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
        ######################################
        # Setup buttons and stuff for Login Page
        # self.ui.actionAdd_Staff.connect(self.showAddStaff)

if __name__ == "__main__":
    dashboard = DashboardWindow()