# Planning to use this script to handle all UI backed functionalities might make more modular in the future


class UI_Functions():
   
    def setTheme(window, file):
        str = open(file,'r').read()
        window.setStyleSheet(str)

    def btn_pb_LoginPage_theme_change():
        print("hllo")
