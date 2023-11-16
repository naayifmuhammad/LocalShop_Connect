class Config:

    __instance = None

    def __init__(self):
        if Config.__instance is not None:
            raise Exception("Config instance exists already!")
        else:
            Config.__instance = self

    @staticmethod
    def getInstance():
        if Config.__instance is None:
            Config()
        return Config.__instance

    @staticmethod
    def getTheme():
        theme = "Themes\default.qss"
        return theme

    @staticmethod
    def setTheme(window, file):
        styleSheet = open(file, 'r').read()
        window.setStyleSheet(styleSheet)
