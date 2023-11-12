import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject
from UI.LoginPage_ui import Ui_Login as Login
from configurations.Config import Config
from modules import main, auth


########################    SLOTS    ########################

def login():
    if (auth.authenticate(Login.label_LoginPage_username, Login.label_LoginPage_password)):
        loginWindow.close()

    else:
        print("Auth failed")


########################    SET SIGNALS    ########################
# Login.pb_LoginPage_login.clicked.connect(login)


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Login()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Login()
        self.ui.setupUi(self)
        main.setTheme(self, Config.theme)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec())
