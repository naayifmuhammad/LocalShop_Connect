from PySide6.QtWidgets import QMainWindow
from models.models import User
from UI.UI_Manager import UI_Manager
import UI.Dashboard
from configurations.Config import Config

cnf = Config.getInstance()

class LoginWindow(QMainWindow):
    dashboard = None
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.LoginUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
        # self.ui.le_loginPage_username.setText("admin")
        # self.ui.le_loginPage_password.setText("admin")
        self.ui.pb_LoginBtn_login.clicked.connect(self.login)
        self.ui.label_LoginPage_register.mousePressEvent = self.goToRegister
        self.show()

    def goToRegister(self,arg):
        #button even here
        pass

    def setDashboard(self,_dashboard):
        self.dashboard = _dashboard

    def login(self):
        loginInfo = (self.ui.le_loginPage_username.text(),self.ui.le_loginPage_password.text())
        if User.login(loginInfo):
            self.dashboard.show()
            cnf.loggedIn = True
            self.close()
        else:
            self.ui.label_IncorrectPasswordLoginPage.setText("Incorrect credentials. Try Again")
            self.ui.le_loginPage_password.clear()
            self.ui.le_loginPage_username.clear()
