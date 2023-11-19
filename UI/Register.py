from PySide6.QtWidgets import QMainWindow
from models.models import User
from UI.UI_Manager import UI_Manager
from configurations.Config import Config

cnf = Config.getInstance()

class RegisterWindow(QMainWindow):


    loginWindow = None

    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.RegisterUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())

        #connect UI elements with functions
        self.ui.pb_gotoLogin.clicked.connect(self.gotoLogin)
        self.ui.pb_submit_btn.clicked.connect(self.register)

    def setComponents(self,loginWindow):
        self.loginWindow = loginWindow


    def gotoLogin(self,arg):
        self.loginWindow.show()
        self.close()

    def isValidNumber(self):
        if User.isNumberValid(self.ui.le_phone_number.text()):
            self.showErrorMessage("Enter a valid phone number")

    def register(self):
        userinfo = (self.ui.le_username.text(),self.ui.le_email.text(),self.ui.le_phone_number.text(),self.ui.le_shopname.text(),self.ui.le_password.text())
        if not self.validInput(userinfo):
            return False
        if User.register(userinfo):
            self.loginWindow.show()
            self.close()
        else:
            self.showErrorMessage("Please Recheck entered information")

    def validInput(self,userinfo):
        if self.isEmpty(userinfo):
            self.showErrorMessage("All fields are mandatory")
            return False

        #username check
        if User.usernameExists(self.ui.le_username.text()):
            self.showErrorMessage("Username already exists")
            return False
        if not User.emailValid(self.ui.le_email.text()):
            self.showErrorMessage("Email not valid")
            return False
        if User.emailExists(self.ui.le_email.text()):
            self.showErrorMessage("Email already exists")
            return False
        if not User.isNumberValid(self.ui.le_phone_number.text()):
            self.showErrorMessage("Enter a valid number")
            return False

        if User.numberExists(self.ui.le_phone_number.text()):
            self.showErrorMessage("Number already exists")
            return False

        if self.ui.le_password.text() != self.ui.le_confirm_pssword.text():
            self.showErrorMessage("Passwords don't match")
            return False
        return True



    def isEmpty(self,userinfo):
        flag = False
        for field in userinfo:
            if field == "":
                flag = True
            if self.ui.le_confirm_pssword.text() == "":
                flag = True
        return flag


    def showErrorMessage(self,error_msg):
        self.ui.label_error_message.setText(error_msg)

