# Planning to use this script to handle all UI backed functionalities might make more modular in the future

def setTheme(window, file):
    str = open(file, 'r').read()
    window.setStyleSheet(str)
