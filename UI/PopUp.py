from PySide6.QtCore import QTimer, Signal
from UI.UI_Manager import UI_Manager
from configurations.Config import Config
from Themes.Themes import Theme
from extras.UI_Functionalities import FrameLessWindow


cnf = Config.getInstance()

class PopUpWindow(FrameLessWindow):
    closed = Signal()
    def __init__(self,msg):
        super().__init__()
        self.ui = UI_Manager.PopUpUI()
        self.ui.setupUi(self)
        self.makeframeLess(True)
        self.setupTitleBar(self)
        self.ui.label_msg.setText(msg)
        cnf.setTheme(self, Theme.PopUp)
        self.timer = QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.emitAndClose)
        self.show()

    def emitAndClose(self):
        self.closed.emit()
        self.close()
    def closeWindow(self, arg):
        self.closed.emit()
        self.close()


