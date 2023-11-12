# -*- coding: utf-8 -*-

######################################################################################################
## Form generated from reading UI file 'Dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
######################################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(703, 458)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_2 = QPushButton(self.frame)
        self.btn_2.setObjectName(u"btn_2")

        self.horizontalLayout.addWidget(self.btn_2)

        self.btn_3 = QPushButton(self.frame)
        self.btn_3.setObjectName(u"btn_3")

        self.horizontalLayout.addWidget(self.btn_3)

        self.btn = QPushButton(self.frame)
        self.btn.setObjectName(u"btn")

        self.horizontalLayout.addWidget(self.btn)

        self.btn_4 = QPushButton(self.frame)
        self.btn_4.setObjectName(u"btn_4")

        self.horizontalLayout.addWidget(self.btn_4)

        self.btn_8 = QPushButton(self.frame)
        self.btn_8.setObjectName(u"btn_8")

        self.horizontalLayout.addWidget(self.btn_8)

        self.btn_7 = QPushButton(self.frame)
        self.btn_7.setObjectName(u"btn_7")

        self.horizontalLayout.addWidget(self.btn_7)

        self.btn_6 = QPushButton(self.frame)
        self.btn_6.setObjectName(u"btn_6")

        self.horizontalLayout.addWidget(self.btn_6)

        self.btn_5 = QPushButton(self.frame)
        self.btn_5.setObjectName(u"btn_5")

        self.horizontalLayout.addWidget(self.btn_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.sidebar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sideNav = QFrame(self.sidebar)
        self.sideNav.setObjectName(u"sideNav")
        self.sideNav.setFrameShape(QFrame.StyledPanel)
        self.sideNav.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sideNav)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.sideNav)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.sideNav)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.sideNav)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.sideNav)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.sideNav)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.sideNav)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.sideNav)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addWidget(self.sideNav)

        self.Dashboard = QFrame(self.sidebar)
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setFrameShape(QFrame.StyledPanel)
        self.Dashboard.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Dashboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.Dashboard)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.Dashboard)


        self.verticalLayout_2.addWidget(self.sidebar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"something", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Another", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Another", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"another", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"another", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"another", None))
    # retranslateUi

