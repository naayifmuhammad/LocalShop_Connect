# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(809, 392)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.label_login_heading = QLabel(self.centralwidget)
        self.label_login_heading.setObjectName(u"label_login_heading")
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(55)
        self.label_login_heading.setFont(font)
        self.label_login_heading.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_login_heading)

        self.le_loginPage_username = QLineEdit(self.centralwidget)
        self.le_loginPage_username.setObjectName(u"le_loginPage_username")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.le_loginPage_username)

        self.le_loginPage_password = QLineEdit(self.centralwidget)
        self.le_loginPage_password.setObjectName(u"le_loginPage_password")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.le_loginPage_password)

        self.pb_LoginPage_login = QPushButton(self.centralwidget)
        self.pb_LoginPage_login.setObjectName(u"pb_LoginPage_login")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.pb_LoginPage_login)

        self.label_LoginPage_register = QLabel(self.centralwidget)
        self.label_LoginPage_register.setObjectName(u"label_LoginPage_register")
        self.label_LoginPage_register.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.label_LoginPage_register)


        self.gridLayout.addLayout(self.formLayout, 0, 2, 1, 1)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_login_heading.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.le_loginPage_username.setPlaceholderText(QCoreApplication.translate("Login", u"Enter username", None))
        self.le_loginPage_password.setPlaceholderText(QCoreApplication.translate("Login", u"Enter password", None))
        self.pb_LoginPage_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_LoginPage_register.setText(QCoreApplication.translate("Login", u"Don't have an account? Register", None))
    # retranslateUi

