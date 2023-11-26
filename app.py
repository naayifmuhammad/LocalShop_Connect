import sys
from PySide6.QtWidgets import QApplication
from UI import Login, Dashboard, AddItem, Register
from configurations.Config import Config

#config SingleTon
cnf = Config.getInstance()



def login():
    dashboardWindow.startMaximised()
    loginWindow.loggedIn.disconnect()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #init windows
    loginWindow = Login.LoginWindow()
    registerWindow = Register.RegisterWindow()
    dashboardWindow = Dashboard.DashboardWindow()
    addItemWindow = AddItem.AddItemDialog()

    #set components
    loginWindow.setComponents(dashboardWindow,registerWindow)
    loginWindow.show()
    loginWindow.loggedIn.connect(login)
    registerWindow.setComponents(loginWindow)
    dashboardWindow.setComponents(addItemWindow)


    sys.exit(app.exec())
