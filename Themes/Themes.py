class Theme:

    UIPath = "Themes/"
    Login = UIPath + "Login.qss"
    Register = UIPath + "Register.qss"
    Dashboard = UIPath + "Dashboard.qss"
    def __init__(self):
        if Theme.__instance is not None:
            raise Exception("Theme instance exists already!")
        else:
            self.loggedIn = False
            Theme.__instance = self
