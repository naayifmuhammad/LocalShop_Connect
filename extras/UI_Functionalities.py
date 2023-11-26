from PySide6 import QtCore
from PySide6.QtCore import QPoint
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QMainWindow, QSizePolicy, QSpacerItem
from configurations.Config import Config
from Themes.Themes import Theme


cnf = Config.getInstance()


class CustomTitleBar(QFrame):

    closeBtn = None
    minimizeBtn = None
    def __init__(self, parent=None,isDarkTheme=False):
        super().__init__(parent)
        self.setObjectName("customTitleBar")
        self.setMaximumHeight(50)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Horizontal Spacer on the Left
        spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer_left)

        #set up the font
        btnFont = QFont()
        btnFont.setFamily("Segoe UI Semibold")
        btnFont.setBold(1)
        btnFont.setPointSize(15)


        # Minimize Button
        self.minimizeBtn = QLabel(self)
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.minimizeBtn.setMinimumSize(20, 0)
        self.minimizeBtn.setFont(btnFont)
        self.minimizeBtn.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)
        self.minimizeBtn.setText(" - ")



        layout.addWidget(self.minimizeBtn)

        # Close Button
        self.closeBtn = QLabel(self)
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.setMinimumSize(20, 0)
        self.closeBtn.setFont(btnFont)
        self.closeBtn.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)
        self.closeBtn.setText(" x ")

        layout.addWidget(self.closeBtn)

        if isDarkTheme:
            cnf.setTheme(self,Theme.customTitle_dark)
        else:
            cnf.setTheme(self,Theme.customTitle)


class FrameLessWindow(QMainWindow):
    def __init__(self):
        self.oldPosition = None
        super().__init__()

    def makeframeLess(self, frameLessFlag):
        if frameLessFlag:
            self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def closeWindow(self, arg):
        self.close()

    def minimizeWindow(self, arg):
        self.showMinimized()

    def setupTitleBar(self,window,isDarkTheme=False):

        self.customTitleBar = CustomTitleBar(window,isDarkTheme)

        # Add the custom title bar to the layout
        window.ui.customTitleSlot.addWidget(self.customTitleBar)

        # Add the existing content to the layout
        window.ui.customTitleSlot.addLayout(window.ui.gridLayout)

        # Set the layout for the main window
        window.setLayout(window.ui.customTitleSlot)
        self.customTitleBar.closeBtn.mousePressEvent = self.closeWindow
        self.customTitleBar.minimizeBtn.mousePressEvent = self.minimizeWindow


