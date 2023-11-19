class Config:

    loggedIn = False
    def __init__(self):
        if Config.__instance is not None:
            raise Exception("Config instance exists already!")
        else:
            self.loggedIn = False
            Config.__instance = self

    @staticmethod
    def getInstance():
        if Config.__instance is None:
            Config()
        return Config.__instance
    __instance = None

    @staticmethod
    def getTheme():
        theme = "Themes/default.qss"
        return theme

    @staticmethod
    def setTheme(window, file):
        styleSheet = open(file, 'r').read()
        window.setStyleSheet(styleSheet)

