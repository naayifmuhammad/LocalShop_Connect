class Theme:

    UIPath = "Themes/"
    Login = UIPath + "Login.qss"
    Register = UIPath + "Register.qss"
    Dashboard = UIPath + "Dashboard.qss"
    customTitle = UIPath + "titleBar.qss"
    customTitle_dark = UIPath + "titleBar_dark.qss"
    PopUp = UIPath + "PopUp.qss"
    sideNavigation = UIPath + "sideNavigation.qss"
    AddProduct = UIPath + "addProduct.qss"
    AddVendor = UIPath + "AddVendor.qss"
    AddCategory = UIPath + "AddVendor.qss"
    def __init__(self):
        if Theme.__instance is not None:
            raise Exception("Theme instance exists already!")
        else:
            self.loggedIn = False
            Theme.__instance = self
    def customTitleBarTheme(darkTheme=True):
        if darkTheme:
            return "Themes/" + "titleBar_dark.qss"
        else:
            return "Themes/" + "titleBar.qss"


