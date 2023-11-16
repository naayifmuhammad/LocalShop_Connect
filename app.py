import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from UI.import_UI import *
from configurations.Config import Config
from modules import main
from models.models import *


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Login()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)
        self.ui.le_loginPage_username.setText("admin")
        self.ui.le_loginPage_password.setText("admin")
        ######################################
        # Setup buttons and stuff for Login Page
        self.ui.pb_LoginBtn_login.clicked.connect(self.login)

    def login(self):
        if User.login(self.ui.le_loginPage_username,self.ui.le_loginPage_password):
            dashboardWindow.show()
            loginWindow.close()


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Dashboard()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)
        ######################################
        # Setup buttons and stuff for Login Page
        # self.ui.actionAdd_Staff.connect(self.showAddStaff)

    # def showAddStaff(self):


class AddNewStaffWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = AddStaffWindow()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)
        ######################################
        # Setup buttons and stuff for add staff Page
        # self.ui.clicked.connect(self.login)


class AddItemDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = AddNewItemWindow()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)
        ######################################
        # Setup buttons and stuff for add staff Page
        # self.ui.clicked.connect(self.login)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    addStaffDialogue = AddNewStaffWindow()
    addNewItemDialog = AddItemDialog()
    dashboardWindow = DashboardWindow()
    sys.exit(app.exec())
