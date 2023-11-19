# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(809, 421)
        self.loginCentralWidget = QWidget(Login)
        self.loginCentralWidget.setObjectName(u"loginCentralWidget")
        self.gridLayout = QGridLayout(self.loginCentralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.LoginGrid = QGridLayout()
        self.LoginGrid.setObjectName(u"LoginGrid")
        self.LoginItems = QFrame(self.loginCentralWidget)
        self.LoginItems.setObjectName(u"LoginItems")
        self.LoginItems.setMinimumSize(QSize(350, 0))
        self.LoginItems.setFrameShape(QFrame.StyledPanel)
        self.LoginItems.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LoginItems)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_login_heading = QLabel(self.LoginItems)
        self.label_login_heading.setObjectName(u"label_login_heading")
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(55)
        self.label_login_heading.setFont(font)
        self.label_login_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_login_heading)

        self.le_loginPage_username = QLineEdit(self.LoginItems)
        self.le_loginPage_username.setObjectName(u"le_loginPage_username")

        self.verticalLayout_2.addWidget(self.le_loginPage_username)

        self.le_loginPage_password = QLineEdit(self.LoginItems)
        self.le_loginPage_password.setObjectName(u"le_loginPage_password")
        self.le_loginPage_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.le_loginPage_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.le_loginPage_password)

        self.label_LoginPage_register = QLabel(self.LoginItems)
        self.label_LoginPage_register.setObjectName(u"label_LoginPage_register")
        self.label_LoginPage_register.setMinimumSize(QSize(0, 24))
        self.label_LoginPage_register.setMaximumSize(QSize(16777215, 15))
        self.label_LoginPage_register.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_LoginPage_register)

        self.pb_LoginBtn_login = QPushButton(self.LoginItems)
        self.pb_LoginBtn_login.setObjectName(u"pb_LoginBtn_login")

        self.verticalLayout_2.addWidget(self.pb_LoginBtn_login)

        self.label_IncorrectPasswordLoginPage = QLabel(self.LoginItems)
        self.label_IncorrectPasswordLoginPage.setObjectName(u"label_IncorrectPasswordLoginPage")
        font1 = QFont()
        font1.setWeight(QFont.Medium)
        self.label_IncorrectPasswordLoginPage.setFont(font1)
        self.label_IncorrectPasswordLoginPage.setStyleSheet(u"color:red")
        self.label_IncorrectPasswordLoginPage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_IncorrectPasswordLoginPage)

        self.verticalSpacer_2 = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.LoginGrid.addWidget(self.LoginItems, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.LoginGrid, 1, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.customSlot = QVBoxLayout()
        self.customSlot.setObjectName(u"customSlot")

        self.gridLayout.addLayout(self.customSlot, 0, 0, 1, 4)

        Login.setCentralWidget(self.loginCentralWidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_login_heading.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.le_loginPage_username.setPlaceholderText(QCoreApplication.translate("Login", u"Enter username", None))
        self.le_loginPage_password.setPlaceholderText(QCoreApplication.translate("Login", u"Enter password", None))
        self.label_LoginPage_register.setText(QCoreApplication.translate("Login", u"Don't have an account? Register", None))
        self.pb_LoginBtn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_IncorrectPasswordLoginPage.setText("")
    # retranslateUi

