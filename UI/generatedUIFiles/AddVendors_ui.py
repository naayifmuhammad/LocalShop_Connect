# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddVendors.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_AddVendor(object):
    def setupUi(self, AddVendor):
        if not AddVendor.objectName():
            AddVendor.setObjectName(u"AddVendor")
        AddVendor.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/button-icons/plus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        AddVendor.setWindowIcon(icon)
        self.actionAdd_new_category = QAction(AddVendor)
        self.actionAdd_new_category.setObjectName(u"actionAdd_new_category")
        self.actionRemove_a_category = QAction(AddVendor)
        self.actionRemove_a_category.setObjectName(u"actionRemove_a_category")
        self.actionAdd_new_vendor = QAction(AddVendor)
        self.actionAdd_new_vendor.setObjectName(u"actionAdd_new_vendor")
        self.actionRemove_existing_vendor = QAction(AddVendor)
        self.actionRemove_existing_vendor.setObjectName(u"actionRemove_existing_vendor")
        self.actionView_Vendors = QAction(AddVendor)
        self.actionView_Vendors.setObjectName(u"actionView_Vendors")
        self.actionView_Categories = QAction(AddVendor)
        self.actionView_Categories.setObjectName(u"actionView_Categories")
        self.actionAdd_Vendors = QAction(AddVendor)
        self.actionAdd_Vendors.setObjectName(u"actionAdd_Vendors")
        self.actionRemove_Vendors = QAction(AddVendor)
        self.actionRemove_Vendors.setObjectName(u"actionRemove_Vendors")
        self.actionAdd_Categories = QAction(AddVendor)
        self.actionAdd_Categories.setObjectName(u"actionAdd_Categories")
        self.actionRemove_Categories = QAction(AddVendor)
        self.actionRemove_Categories.setObjectName(u"actionRemove_Categories")
        self.centralwidget = QWidget(AddVendor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.Main = QFrame(self.centralwidget)
        self.Main.setObjectName(u"Main")
        self.Main.setMinimumSize(QSize(596, 400))
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLabel = QLabel(self.Main)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setMaximumSize(QSize(16777215, 111))
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(37)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.headerLabel)

        self.frame = QFrame(self.Main)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.InputFields = QFrame(self.frame)
        self.InputFields.setObjectName(u"InputFields")
        self.InputFields.setFrameShape(QFrame.StyledPanel)
        self.InputFields.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.InputFields)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vendorName = QLineEdit(self.InputFields)
        self.vendorName.setObjectName(u"vendorName")
        self.vendorName.setProperty("mandatory", True)

        self.verticalLayout_3.addWidget(self.vendorName)

        self.ownerName = QLineEdit(self.InputFields)
        self.ownerName.setObjectName(u"ownerName")
        self.ownerName.setProperty("mandatory", False)

        self.verticalLayout_3.addWidget(self.ownerName)

        self.location = QLineEdit(self.InputFields)
        self.location.setObjectName(u"location")
        self.location.setProperty("mandatory", False)

        self.verticalLayout_3.addWidget(self.location)


        self.horizontalLayout_2.addWidget(self.InputFields)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.Main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add = QPushButton(self.frame_3)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.cancel = QPushButton(self.frame_3)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.Main, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        AddVendor.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.vendorName, self.ownerName)
        QWidget.setTabOrder(self.ownerName, self.location)

        self.retranslateUi(AddVendor)

        QMetaObject.connectSlotsByName(AddVendor)
    # setupUi

    def retranslateUi(self, AddVendor):
        AddVendor.setWindowTitle(QCoreApplication.translate("AddVendor", u"Add Vendor", None))
        self.actionAdd_new_category.setText(QCoreApplication.translate("AddVendor", u"Add new category", None))
        self.actionRemove_a_category.setText(QCoreApplication.translate("AddVendor", u"Remove a category", None))
        self.actionAdd_new_vendor.setText(QCoreApplication.translate("AddVendor", u"Add new vendor", None))
        self.actionRemove_existing_vendor.setText(QCoreApplication.translate("AddVendor", u"Remove existing vendor", None))
        self.actionView_Vendors.setText(QCoreApplication.translate("AddVendor", u"View Vendors", None))
        self.actionView_Categories.setText(QCoreApplication.translate("AddVendor", u"View Categories", None))
        self.actionAdd_Vendors.setText(QCoreApplication.translate("AddVendor", u"Add Vendors", None))
        self.actionRemove_Vendors.setText(QCoreApplication.translate("AddVendor", u"Remove Vendors", None))
        self.actionAdd_Categories.setText(QCoreApplication.translate("AddVendor", u"Add Categories", None))
        self.actionRemove_Categories.setText(QCoreApplication.translate("AddVendor", u"Remove Categories", None))
        self.headerLabel.setText(QCoreApplication.translate("AddVendor", u"Add New Vendor", None))
        self.vendorName.setPlaceholderText(QCoreApplication.translate("AddVendor", u"Vendor Name *", None))
        self.ownerName.setPlaceholderText(QCoreApplication.translate("AddVendor", u"Shop Owner Name", None))
        self.location.setPlaceholderText(QCoreApplication.translate("AddVendor", u"Location", None))
        self.add.setText(QCoreApplication.translate("AddVendor", u"Add", None))
        self.cancel.setText(QCoreApplication.translate("AddVendor", u"Cancel", None))
    # retranslateUi

