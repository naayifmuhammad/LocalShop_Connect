from PySide6.QtWidgets import QDialog
from UI.UI_Manager import UI_Manager

from configurations.Config import Config

cnf = Config.getInstance()

class AddNewStaffWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.AddStaffUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
        ######################################
        # Setup buttons and stuff for add staff Page
        # self.ui.clicked.connect(self.login)