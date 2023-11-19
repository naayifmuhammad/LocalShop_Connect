from PySide6.QtWidgets import QDialog
from models.models import User
from UI.UI_Manager import UI_Manager
import UI.Dashboard

from configurations.Config import Config

cnf = Config.getInstance()

class AddItemDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_Manager.AddItemUI()
        self.ui.setupUi(self)
        cnf.setTheme(self, cnf.getTheme())
        ######################################
        # Setup buttons and stuff for add staff Page
        # self.ui.clicked.connect(self.login)