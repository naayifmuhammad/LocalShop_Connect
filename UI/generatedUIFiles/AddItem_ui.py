# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddItem.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddNewStaffDialog(object):
    def setupUi(self, AddNewStaffDialog):
        if not AddNewStaffDialog.objectName():
            AddNewStaffDialog.setObjectName(u"AddNewStaffDialog")
        AddNewStaffDialog.resize(611, 416)
        self.AddStaff = QFrame(AddNewStaffDialog)
        self.AddStaff.setObjectName(u"AddStaff")
        self.AddStaff.setGeometry(QRect(40, 10, 551, 391))
        self.AddStaff.setFrameShape(QFrame.StyledPanel)
        self.AddStaff.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.AddStaff)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(self.AddStaff)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.qlabelAddStaff = QLabel(self.AddStaff)
        self.qlabelAddStaff.setObjectName(u"qlabelAddStaff")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.qlabelAddStaff.setFont(font)
        self.qlabelAddStaff.setLayoutDirection(Qt.LeftToRight)
        self.qlabelAddStaff.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.qlabelAddStaff)

        self.leEnterStaffName = QLineEdit(self.AddStaff)
        self.leEnterStaffName.setObjectName(u"leEnterStaffName")

        self.verticalLayout.addWidget(self.leEnterStaffName)

        self.lineEdit = QLineEdit(self.AddStaff)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_4 = QLineEdit(self.AddStaff)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_2 = QLineEdit(self.AddStaff)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.AddStaff)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_5 = QLineEdit(self.AddStaff)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.frame = QFrame(self.AddStaff)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.AddStaff)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(250, 150))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(250, 150))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_2)

        self.line_2 = QFrame(self.AddStaff)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)


        self.retranslateUi(AddNewStaffDialog)

        QMetaObject.connectSlotsByName(AddNewStaffDialog)
    # setupUi

    def retranslateUi(self, AddNewStaffDialog):
        AddNewStaffDialog.setWindowTitle(QCoreApplication.translate("AddNewStaffDialog", u"Dialog", None))
        self.qlabelAddStaff.setText(QCoreApplication.translate("AddNewStaffDialog", u"Add New Item", None))
        self.leEnterStaffName.setPlaceholderText(QCoreApplication.translate("AddNewStaffDialog", u"Product ID", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("AddNewStaffDialog", u"Product Name", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("AddNewStaffDialog", u"Purchase Price", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("AddNewStaffDialog", u"Retail Price", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("AddNewStaffDialog", u"Description", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("AddNewStaffDialog", u"Quantity", None))
        self.pushButton_2.setText(QCoreApplication.translate("AddNewStaffDialog", u"Submit", None))
        self.pushButton.setText(QCoreApplication.translate("AddNewStaffDialog", u"Cancel", None))
    # retranslateUi

