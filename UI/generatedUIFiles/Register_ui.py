# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(795, 551)
        self.registerCentralWidget = QWidget(RegisterWindow)
        self.registerCentralWidget.setObjectName(u"registerCentralWidget")
        self.gridLayout = QGridLayout(self.registerCentralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LeftSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.LeftSpacer, 1, 0, 1, 1)

        self.RightSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.RightSpacer, 1, 2, 1, 1)

        self.MainFrame = QFrame(self.registerCentralWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_Register_heading = QLabel(self.MainFrame)
        self.label_Register_heading.setObjectName(u"label_Register_heading")
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(55)
        self.label_Register_heading.setFont(font)
        self.label_Register_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Register_heading)

        self.frame = QFrame(self.MainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_password = QLineEdit(self.frame)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setInputMethodHints(Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.le_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_2.addWidget(self.le_password, 4, 0, 1, 2)

        self.le_email = QLineEdit(self.frame)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.gridLayout_2.addWidget(self.le_email, 3, 0, 1, 1)

        self.le_shopname = QLineEdit(self.frame)
        self.le_shopname.setObjectName(u"le_shopname")

        self.gridLayout_2.addWidget(self.le_shopname, 0, 1, 1, 1)

        self.le_username = QLineEdit(self.frame)
        self.le_username.setObjectName(u"le_username")

        self.gridLayout_2.addWidget(self.le_username, 0, 0, 1, 1)

        self.le_phone_number = QLineEdit(self.frame)
        self.le_phone_number.setObjectName(u"le_phone_number")
        self.le_phone_number.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.le_phone_number.setMaxLength(10)

        self.gridLayout_2.addWidget(self.le_phone_number, 3, 1, 1, 1)

        self.pb_submit_btn = QPushButton(self.frame)
        self.pb_submit_btn.setObjectName(u"pb_submit_btn")

        self.gridLayout_2.addWidget(self.pb_submit_btn, 6, 0, 1, 1)

        self.pb_gotoLogin = QPushButton(self.frame)
        self.pb_gotoLogin.setObjectName(u"pb_gotoLogin")

        self.gridLayout_2.addWidget(self.pb_gotoLogin, 6, 1, 1, 1)

        self.le_confirm_pssword = QLineEdit(self.frame)
        self.le_confirm_pssword.setObjectName(u"le_confirm_pssword")
        self.le_confirm_pssword.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.le_confirm_pssword, 5, 0, 1, 2)

        self.label_error_message = QLabel(self.frame)
        self.label_error_message.setObjectName(u"label_error_message")
        self.label_error_message.setMaximumSize(QSize(16777215, 20))
        self.label_error_message.setStyleSheet(u"color:red")
        self.label_error_message.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_error_message, 7, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame)


        self.gridLayout.addWidget(self.MainFrame, 1, 1, 1, 1)

        self.customTitleSlot = QVBoxLayout()
        self.customTitleSlot.setObjectName(u"customTitleSlot")

        self.gridLayout.addLayout(self.customTitleSlot, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        RegisterWindow.setCentralWidget(self.registerCentralWidget)
        QWidget.setTabOrder(self.le_username, self.le_shopname)
        QWidget.setTabOrder(self.le_shopname, self.le_email)
        QWidget.setTabOrder(self.le_email, self.le_phone_number)
        QWidget.setTabOrder(self.le_phone_number, self.le_password)
        QWidget.setTabOrder(self.le_password, self.le_confirm_pssword)
        QWidget.setTabOrder(self.le_confirm_pssword, self.pb_submit_btn)
        QWidget.setTabOrder(self.pb_submit_btn, self.pb_gotoLogin)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.label_Register_heading.setText(QCoreApplication.translate("RegisterWindow", u"REGISTER", None))
        self.le_password.setText("")
        self.le_password.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Enter secure password", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Enter email", None))
        self.le_shopname.setText("")
        self.le_shopname.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Shop Name", None))
        self.le_username.setText("")
        self.le_username.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Enter username", None))
        self.le_phone_number.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Phone Number", None))
        self.pb_submit_btn.setText(QCoreApplication.translate("RegisterWindow", u"Create account", None))
        self.pb_gotoLogin.setText(QCoreApplication.translate("RegisterWindow", u"Already have an account? Login", None))
        self.le_confirm_pssword.setText("")
        self.le_confirm_pssword.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Confirm Password", None))
        self.label_error_message.setText("")
    # retranslateUi

