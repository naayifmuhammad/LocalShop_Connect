# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(746, 592)
        self.actionSettings = QAction(Dashboard)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionLog_out = QAction(Dashboard)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.actionAdd_staff = QAction(Dashboard)
        self.actionAdd_staff.setObjectName(u"actionAdd_staff")
        self.actionAdd_category = QAction(Dashboard)
        self.actionAdd_category.setObjectName(u"actionAdd_category")
        self.actionItem = QAction(Dashboard)
        self.actionItem.setObjectName(u"actionItem")
        self.actionStaff = QAction(Dashboard)
        self.actionStaff.setObjectName(u"actionStaff")
        self.actionItem_2 = QAction(Dashboard)
        self.actionItem_2.setObjectName(u"actionItem_2")
        self.actionCategory = QAction(Dashboard)
        self.actionCategory.setObjectName(u"actionCategory")
        self.actionItem_3 = QAction(Dashboard)
        self.actionItem_3.setObjectName(u"actionItem_3")
        self.actionCategory_2 = QAction(Dashboard)
        self.actionCategory_2.setObjectName(u"actionCategory_2")
        self.actionAdd_Staff = QAction(Dashboard)
        self.actionAdd_Staff.setObjectName(u"actionAdd_Staff")
        self.actionRemove_Staff = QAction(Dashboard)
        self.actionRemove_Staff.setObjectName(u"actionRemove_Staff")
        self.dashboardCentralWidget = QWidget(Dashboard)
        self.dashboardCentralWidget.setObjectName(u"dashboardCentralWidget")
        self.verticalLayout = QVBoxLayout(self.dashboardCentralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.customTitleSlot = QVBoxLayout()
        self.customTitleSlot.setObjectName(u"customTitleSlot")

        self.verticalLayout.addLayout(self.customTitleSlot)

        self.mainLayout = QGridLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.window2ColumnLayoutVertical = QHBoxLayout()
        self.window2ColumnLayoutVertical.setObjectName(u"window2ColumnLayoutVertical")
        self.itemAddRow = QFrame(self.dashboardCentralWidget)
        self.itemAddRow.setObjectName(u"itemAddRow")
        self.itemAddRow.setFrameShape(QFrame.StyledPanel)
        self.itemAddRow.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.itemAddRow)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ItemDetails = QFrame(self.itemAddRow)
        self.ItemDetails.setObjectName(u"ItemDetails")
        self.ItemDetails.setFrameShape(QFrame.StyledPanel)
        self.ItemDetails.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ItemDetails)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.itemNo = QLineEdit(self.ItemDetails)
        self.itemNo.setObjectName(u"itemNo")

        self.horizontalLayout_2.addWidget(self.itemNo)

        self.ProductCode = QLineEdit(self.ItemDetails)
        self.ProductCode.setObjectName(u"ProductCode")

        self.horizontalLayout_2.addWidget(self.ProductCode)

        self.HSNCode = QLineEdit(self.ItemDetails)
        self.HSNCode.setObjectName(u"HSNCode")

        self.horizontalLayout_2.addWidget(self.HSNCode)

        self.SalePrice = QLineEdit(self.ItemDetails)
        self.SalePrice.setObjectName(u"SalePrice")

        self.horizontalLayout_2.addWidget(self.SalePrice)

        self.Quanitity = QLineEdit(self.ItemDetails)
        self.Quanitity.setObjectName(u"Quanitity")

        self.horizontalLayout_2.addWidget(self.Quanitity)

        self.Discount = QLineEdit(self.ItemDetails)
        self.Discount.setObjectName(u"Discount")

        self.horizontalLayout_2.addWidget(self.Discount)

        self.Amount = QLineEdit(self.ItemDetails)
        self.Amount.setObjectName(u"Amount")

        self.horizontalLayout_2.addWidget(self.Amount)


        self.verticalLayout_5.addWidget(self.ItemDetails)

        self.taxDetails = QFrame(self.itemAddRow)
        self.taxDetails.setObjectName(u"taxDetails")
        self.taxDetails.setFrameShape(QFrame.StyledPanel)
        self.taxDetails.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.taxDetails)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_8 = QLineEdit(self.taxDetails)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_3.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.taxDetails)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_3.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.taxDetails)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_3.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.taxDetails)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_3.addWidget(self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.taxDetails)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_3.addWidget(self.lineEdit_12)


        self.verticalLayout_5.addWidget(self.taxDetails)

        self.confirmAddItemFrame = QFrame(self.itemAddRow)
        self.confirmAddItemFrame.setObjectName(u"confirmAddItemFrame")
        self.confirmAddItemFrame.setFrameShape(QFrame.StyledPanel)
        self.confirmAddItemFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.confirmAddItemFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addItemBtn = QPushButton(self.confirmAddItemFrame)
        self.addItemBtn.setObjectName(u"addItemBtn")

        self.horizontalLayout.addWidget(self.addItemBtn)

        self.cancelBtn = QPushButton(self.confirmAddItemFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout_5.addWidget(self.confirmAddItemFrame)

        self.CartFrame = QFrame(self.itemAddRow)
        self.CartFrame.setObjectName(u"CartFrame")
        self.CartFrame.setFrameShape(QFrame.StyledPanel)
        self.CartFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.CartFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cartView = QTableView(self.CartFrame)
        self.cartView.setObjectName(u"cartView")
        self.cartView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cartView.setAlternatingRowColors(True)
        self.cartView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cartView.setShowGrid(False)
        self.cartView.setGridStyle(Qt.NoPen)
        self.cartView.setSortingEnabled(True)
        self.cartView.setCornerButtonEnabled(True)
        self.cartView.horizontalHeader().setVisible(True)
        self.cartView.horizontalHeader().setStretchLastSection(True)
        self.cartView.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.cartView, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.CartFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.window2ColumnLayoutVertical.addWidget(self.itemAddRow)


        self.mainLayout.addLayout(self.window2ColumnLayoutVertical, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.mainLayout)

        Dashboard.setCentralWidget(self.dashboardCentralWidget)
        QWidget.setTabOrder(self.itemNo, self.ProductCode)
        QWidget.setTabOrder(self.ProductCode, self.HSNCode)
        QWidget.setTabOrder(self.HSNCode, self.SalePrice)
        QWidget.setTabOrder(self.SalePrice, self.Quanitity)
        QWidget.setTabOrder(self.Quanitity, self.Discount)
        QWidget.setTabOrder(self.Discount, self.cancelBtn)
        QWidget.setTabOrder(self.cancelBtn, self.addItemBtn)
        QWidget.setTabOrder(self.addItemBtn, self.cartView)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"MainWindow", None))
        self.actionSettings.setText(QCoreApplication.translate("Dashboard", u"Settings", None))
        self.actionLog_out.setText(QCoreApplication.translate("Dashboard", u"Log out", None))
        self.actionAdd_staff.setText(QCoreApplication.translate("Dashboard", u"Add staff", None))
        self.actionAdd_category.setText(QCoreApplication.translate("Dashboard", u"Add category", None))
        self.actionItem.setText(QCoreApplication.translate("Dashboard", u"Item", None))
        self.actionStaff.setText(QCoreApplication.translate("Dashboard", u"Category", None))
        self.actionItem_2.setText(QCoreApplication.translate("Dashboard", u"Item", None))
        self.actionCategory.setText(QCoreApplication.translate("Dashboard", u"Category", None))
        self.actionItem_3.setText(QCoreApplication.translate("Dashboard", u"Item", None))
        self.actionCategory_2.setText(QCoreApplication.translate("Dashboard", u"Category", None))
        self.actionAdd_Staff.setText(QCoreApplication.translate("Dashboard", u"Add Staff", None))
        self.actionRemove_Staff.setText(QCoreApplication.translate("Dashboard", u"Remove Staff", None))
        self.itemNo.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Item No", None))
        self.ProductCode.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Product Code", None))
        self.HSNCode.setPlaceholderText(QCoreApplication.translate("Dashboard", u"HSN Code", None))
        self.SalePrice.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Sale Price", None))
        self.Quanitity.setText("")
        self.Quanitity.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Quantity", None))
        self.Discount.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Discount", None))
        self.Amount.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Amount", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Dashboard", u"CGST", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Dashboard", u"SGST", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("Dashboard", u"IGST", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Total Tax", None))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Grand Total", None))
        self.addItemBtn.setText(QCoreApplication.translate("Dashboard", u"Add Item", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dashboard", u"Cancel Item", None))
    # retranslateUi

