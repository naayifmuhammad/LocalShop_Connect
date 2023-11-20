from UI.generatedUIFiles.LoginPage_ui import Ui_Login as Login
from UI.generatedUIFiles.Dashboard_ui import Ui_Dashboard as Dashboard
from UI.generatedUIFiles.AddNewStaff_ui import Ui_AddNewStaffDialog as AddStaffWindow
from UI.generatedUIFiles.AddItem_ui import Ui_AddNewStaffDialog as AddNewItemWindow
from UI.generatedUIFiles.Register_ui import Ui_RegisterWindow as RegisterWindow
from UI.generatedUIFiles.PopUp_ui import Ui_PopUp

class UI_Manager:

    __instance = None
    LoginUI = Login
    DashboardUI = Dashboard
    AddStaffUI = AddStaffWindow
    AddItemUI = AddNewItemWindow
    RegisterUI = RegisterWindow
    PopUpUI = Ui_PopUp


    def __init__(self):
        if UI_Manager.__instance is not None:
            raise Exception("UI_Manager instance exists already!")
        else:
            UI_Manager.__instance = self

    @staticmethod
    def getInstance():
        if UI_Manager.__instance is None:
            UI_Manager()
        return UI_Manager.__instance


