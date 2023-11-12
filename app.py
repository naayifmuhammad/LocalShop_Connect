import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject
from UI.LoginPage_ui import Ui_Login as Login
from UI.Dashboard_ui import Ui_Dashboard as Dashboard
from configurations.Config import Config
from modules import main, auth


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Login()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)
        ######################################
        #Setup buttons and stuff for Login Page
        self.ui.pb_LoginBtn_login.clicked.connect(self.login)

    def login(self):
        success = auth.authenticate(self.ui.le_loginPage_username.text(), self.ui.le_loginPage_password.text())
        if success:
            dashboardWindow.show()
            loginWindow.close()
            self.ui.label_LoginPage_register.setText("Success")


        else:
            self.ui.label_LoginPage_register.setText("Failed")




class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Dashboard()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    dashboardWindow = DashboardWindow()
    sys.exit(app.exec())