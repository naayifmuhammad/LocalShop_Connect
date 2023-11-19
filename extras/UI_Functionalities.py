from PySide6 import QtCore
from PySide6.QtCore import QPoint
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QMainWindow, QSizePolicy, QSpacerItem

class CustomTitleBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("customTitleBar")
        self.setMaximumHeight(50)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Horizontal Spacer on the Left
        spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer_left)

        # Minimize Button
        self.minimizeBtn = QLabel(self)
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.minimizeBtn.setMinimumSize(20, 0)
        self.minimizeBtn.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)
        self.minimizeBtn.setText("-")

        layout.addWidget(self.minimizeBtn)

        # Close Button
        self.closeBtn = QLabel(self)
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.setMinimumSize(20, 0)
        self.closeBtn.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)
        self.closeBtn.setText("x")

        layout.addWidget(self.closeBtn)


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

    def setupTitleBar(self):
        # Use the CustomTitleBar class you defined
        self.customTitleBar = CustomTitleBar(self)
        self.customTitleBar.setObjectName("customTitleBar")
        self.customTitleBar.setMaximumSize(16777215, 50)

        # Add the custom title bar to the layout
        self.horizontalLayout = QHBoxLayout(self.customTitleBar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_3)
        self.horizontalLayout.addWidget(self.customTitleBar)
