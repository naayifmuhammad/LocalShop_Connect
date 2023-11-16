import sys
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from configurations.Config import Config
from models.models import User
from UI.UI_Manager import UI_Manager

#config SingleTon
cnf = Config.getInstance()


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.LoginUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
        # self.ui.le_loginPage_username.setText("admin")
        # self.ui.le_loginPage_password.setText("admin")
        self.ui.pb_LoginBtn_login.clicked.connect(self.login)
        self.ui.label_LoginPage_register.mousePressEvent = (self.goToRegister)


    def goToRegister(self,arg):
        #button even here
        pass


    def login(self):
        loginInfo = (self.ui.le_loginPage_username.text(),self.ui.le_loginPage_password.text())
        if User.login(loginInfo):
            dashboardWindow.show()
            loginWindow.close()
        else:
            self.ui.label_IncorrectPasswordLoginPage.setText("Incorrect credentials. Try Again")
            self.ui.le_loginPage_password.clear()
            self.ui.le_loginPage_username.clear()


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.DashboardUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
        ######################################
        # Setup buttons and stuff for Login Page
        # self.ui.actionAdd_Staff.connect(self.showAddStaff)

    # def showAddStaff(self):


class AddNewStaffWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.AddStaffUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
        ######################################
        # Setup buttons and stuff for add staff Page
        # self.ui.clicked.connect(self.login)


class AddItemDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.AddItemUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
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
