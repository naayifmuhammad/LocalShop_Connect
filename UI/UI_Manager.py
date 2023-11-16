from UI.LoginPage_ui import Ui_Login as Login
from UI.Dashboard_ui import Ui_Dashboard as Dashboard
from UI.AddNewStaff_ui import Ui_AddNewStaffDialog as AddStaffWindow
from UI.AddItem_ui import Ui_AddNewStaffDialog as AddNewItemWindow
from UI.Register_ui import Ui_RegisterWindow as RegisterWindow

from enum import Enum

class UI_Manager:

    __instance = None
    LoginUI = Login
    DashboardUI = Dashboard
    AddStaffUI = AddStaffWindow
    AddItemUI = AddNewItemWindow
    RegisterUI = RegisterWindow

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


