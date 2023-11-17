import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
#from UI.Login import LoginWindow
import UI.Login
from UI.Dashboard import DashboardWindow
from configurations.Config import Config
from UI.UI_Manager import UI_Manager

#config SingleTon
cnf = Config.getInstance()


#
# class AddNewStaffWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.ui = UI_Manager.AddStaffUI()
#         self.ui.setupUi(self)
#         cnf.setTheme(self, cnf.getTheme())
#         ######################################
#         # Setup buttons and stuff for add staff Page
#         # self.ui.clicked.connect(self.login)
#
#
# class AddItemDialog(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.ui = UI_Manager.AddItemUI()
#         self.ui.setupUi(self)
#         cnf.setTheme(self, cnf.getTheme())
#         ######################################
#         # Setup buttons and stuff for add staff Page
#         # self.ui.clicked.connect(self.login)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = UI.Login.LoginWindow()
    dashboardWindow = DashboardWindow()
    loginWindow.setDashboard(dashboardWindow)
    sys.exit(app.exec())
