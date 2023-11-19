from PySide6.QtWidgets import QVBoxLayout

from models.models import User
from UI.UI_Manager import UI_Manager
from configurations.Config import Config
from Themes.Themes import Theme
from extras.UI_Functionalities import FrameLessWindow, CustomTitleBar

cnf = Config.getInstance()

class LoginWindow(FrameLessWindow):

    dashboardWindow = None
    registerWindow = None

    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.LoginUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.makeframeLess(True)
        self.setupTitleBar(self)

        cnf.setTheme(self, Theme.Login)
        self.ui.le_loginPage_username.setText("admin")
        self.ui.le_loginPage_password.setText("admin")




        self.ui.pb_LoginBtn_login.clicked.connect(self.login)
        self.ui.label_LoginPage_register.mousePressEvent = self.goToRegister
        self.show()

    def goToRegister(self,arg):
        self.registerWindow.show()
        self.close()




    def setComponents(self,dashboard,register):
        self.dashboardWindow = dashboard
        self.registerWindow = register


    def login(self):
        loginInfo = (self.ui.le_loginPage_username.text(),self.ui.le_loginPage_password.text())
        if User.login(loginInfo):
            self.dashboardWindow.show()
            cnf.loggedIn = True
            self.close()
        else:
            self.ui.label_IncorrectPasswordLoginPage.setText("Incorrect credentials. Try Again")
            self.ui.le_loginPage_password.clear()
            self.ui.le_loginPage_username.clear()
