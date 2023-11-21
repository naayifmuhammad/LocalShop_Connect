from models.models import User
from UI.UI_Manager import UI_Manager
from configurations.Config import Config
from extras.UI_Functionalities import FrameLessWindow
from Themes.Themes import Theme
from UI.PopUp import PopUpWindow

cnf = Config.getInstance()

class RegisterWindow(FrameLessWindow):


    loginWindow = None
    popUp = None

    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.RegisterUI()
        self.ui.setupUi(self)
        self.makeframeLess(True)
        self.setupTitleBar(self)
        cnf.setTheme(self,Theme.Register )

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

        # once Popup disappears do this

    def afterPopUp(self):
        self.popUp.closed.disconnect()
        self.loginWindow.show()


    def register(self):
        userinfo = (self.ui.le_username.text(),self.ui.le_email.text(),self.ui.le_phone_number.text(),self.ui.le_shopname.text(),self.ui.le_password.text())
        if not self.validInput(userinfo):
            return False
        if User.register(userinfo):
            self.popUp = PopUpWindow("Registration successfully completed")
            self.popUp.closed.connect(self.afterPopUp)
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

