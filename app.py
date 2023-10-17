import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject
from UI.LoginPage_ui import Ui_MainWindow
from configurations.Config import Config
from Functions.UI_Functions import *


class MyMainWindow(QMainWindow):
    

            
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)  
        UI_Functions.setTheme(self,Config.theme)

        #########################
        ##buttons and actions
        self.ui.pb_LoginPage_theme_change.clicked.connect(UI_Functions.btn_pb_LoginPage_theme_change)

        #########################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())
