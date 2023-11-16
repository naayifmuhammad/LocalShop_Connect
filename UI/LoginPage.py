

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