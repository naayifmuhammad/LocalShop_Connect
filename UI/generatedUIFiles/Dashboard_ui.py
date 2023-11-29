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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)
import icons_rc

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
        self.Main = QHBoxLayout()
        self.Main.setObjectName(u"Main")
        self.sideNavigation = QFrame(self.dashboardCentralWidget)
        self.sideNavigation.setObjectName(u"sideNavigation")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideNavigation.sizePolicy().hasHeightForWidth())
        self.sideNavigation.setSizePolicy(sizePolicy)
        self.sideNavigation.setMinimumSize(QSize(0, 0))
        self.sideNavigation.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgb(208, 208, 208);\n"
"}")
        self.sideNavigation.setFrameShape(QFrame.StyledPanel)
        self.sideNavigation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sideNavigation)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hamburger = QPushButton(self.sideNavigation)
        self.hamburger.setObjectName(u"hamburger")
        self.hamburger.setLayoutDirection(Qt.LeftToRight)
        self.hamburger.setStyleSheet(u"text-align:left;")
        icon = QIcon()
        icon.addFile(u":/button-icons/hamburger-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hamburger.setIcon(icon)
        self.hamburger.setIconSize(QSize(25, 25))
        self.hamburger.setAutoDefault(False)
        self.hamburger.setFlat(True)

        self.verticalLayout_2.addWidget(self.hamburger)

        self.billing = QPushButton(self.sideNavigation)
        self.billing.setObjectName(u"billing")
        self.billing.setLayoutDirection(Qt.LeftToRight)
        self.billing.setStyleSheet(u"text-align:left;")
        icon1 = QIcon()
        icon1.addFile(u":/button-icons/billing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.billing.setIcon(icon1)
        self.billing.setIconSize(QSize(25, 25))
        self.billing.setFlat(True)

        self.verticalLayout_2.addWidget(self.billing)

        self.products = QPushButton(self.sideNavigation)
        self.products.setObjectName(u"products")
        self.products.setLayoutDirection(Qt.LeftToRight)
        self.products.setStyleSheet(u"text-align:left;")
        icon2 = QIcon()
        icon2.addFile(u":/button-icons/features.png", QSize(), QIcon.Normal, QIcon.Off)
        self.products.setIcon(icon2)
        self.products.setIconSize(QSize(25, 25))
        self.products.setFlat(True)

        self.verticalLayout_2.addWidget(self.products)

        self.staff = QPushButton(self.sideNavigation)
        self.staff.setObjectName(u"staff")
        self.staff.setLayoutDirection(Qt.LeftToRight)
        self.staff.setStyleSheet(u"text-align:left;")
        icon3 = QIcon()
        icon3.addFile(u":/button-icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.staff.setIcon(icon3)
        self.staff.setIconSize(QSize(25, 25))
        self.staff.setFlat(True)

        self.verticalLayout_2.addWidget(self.staff)

        self.analytics = QPushButton(self.sideNavigation)
        self.analytics.setObjectName(u"analytics")
        self.analytics.setLayoutDirection(Qt.LeftToRight)
        self.analytics.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/button-icons/analytics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analytics.setIcon(icon4)
        self.analytics.setIconSize(QSize(25, 25))
        self.analytics.setFlat(True)

        self.verticalLayout_2.addWidget(self.analytics)

        self.history = QPushButton(self.sideNavigation)
        self.history.setObjectName(u"history")
        self.history.setLayoutDirection(Qt.LeftToRight)
        self.history.setStyleSheet(u"text-align:left;")
        icon5 = QIcon()
        icon5.addFile(u":/button-icons/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.history.setIcon(icon5)
        self.history.setIconSize(QSize(25, 25))
        self.history.setFlat(True)

        self.verticalLayout_2.addWidget(self.history)

        self.settings = QPushButton(self.sideNavigation)
        self.settings.setObjectName(u"settings")
        self.settings.setLayoutDirection(Qt.LeftToRight)
        self.settings.setStyleSheet(u"text-align:left;")
        icon6 = QIcon()
        icon6.addFile(u":/button-icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon6)
        self.settings.setIconSize(QSize(25, 25))
        self.settings.setFlat(True)

        self.verticalLayout_2.addWidget(self.settings)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.Main.addWidget(self.sideNavigation)

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
        self.itemNo.setMaximumSize(QSize(50, 16777215))
        self.itemNo.setProperty("editable", False)

        self.horizontalLayout_2.addWidget(self.itemNo)

        self.ProductCode = QComboBox(self.ItemDetails)
        self.ProductCode.setObjectName(u"ProductCode")

        self.horizontalLayout_2.addWidget(self.ProductCode)

        self.HSNCode = QLineEdit(self.ItemDetails)
        self.HSNCode.setObjectName(u"HSNCode")
        self.HSNCode.setProperty("editable", False)

        self.horizontalLayout_2.addWidget(self.HSNCode)

        self.SalePrice = QLineEdit(self.ItemDetails)
        self.SalePrice.setObjectName(u"SalePrice")
        self.SalePrice.setProperty("editable", False)

        self.horizontalLayout_2.addWidget(self.SalePrice)

        self.Quantity = QLineEdit(self.ItemDetails)
        self.Quantity.setObjectName(u"Quantity")
        self.Quantity.setProperty("editable", True)

        self.horizontalLayout_2.addWidget(self.Quantity)

        self.Discount = QLineEdit(self.ItemDetails)
        self.Discount.setObjectName(u"Discount")
        self.Discount.setProperty("editable", True)

        self.horizontalLayout_2.addWidget(self.Discount)

        self.Amount = QLineEdit(self.ItemDetails)
        self.Amount.setObjectName(u"Amount")
        self.Amount.setProperty("editable", False)

        self.horizontalLayout_2.addWidget(self.Amount)


        self.verticalLayout_5.addWidget(self.ItemDetails)

        self.taxDetails = QFrame(self.itemAddRow)
        self.taxDetails.setObjectName(u"taxDetails")
        self.taxDetails.setFrameShape(QFrame.StyledPanel)
        self.taxDetails.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.taxDetails)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cgst = QLineEdit(self.taxDetails)
        self.cgst.setObjectName(u"cgst")
        self.cgst.setProperty("editable", False)

        self.horizontalLayout_3.addWidget(self.cgst)

        self.sgst = QLineEdit(self.taxDetails)
        self.sgst.setObjectName(u"sgst")
        self.sgst.setProperty("editable", False)

        self.horizontalLayout_3.addWidget(self.sgst)

        self.igst = QLineEdit(self.taxDetails)
        self.igst.setObjectName(u"igst")
        self.igst.setProperty("editable", False)

        self.horizontalLayout_3.addWidget(self.igst)

        self.totalTax = QLineEdit(self.taxDetails)
        self.totalTax.setObjectName(u"totalTax")
        self.totalTax.setProperty("editable", False)

        self.horizontalLayout_3.addWidget(self.totalTax)

        self.grandTotal = QLineEdit(self.taxDetails)
        self.grandTotal.setObjectName(u"grandTotal")
        self.grandTotal.setProperty("editable", False)

        self.horizontalLayout_3.addWidget(self.grandTotal)


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
        self.confirmBillBtn = QPushButton(self.CartFrame)
        self.confirmBillBtn.setObjectName(u"confirmBillBtn")

        self.gridLayout.addWidget(self.confirmBillBtn, 1, 1, 1, 1)

        self.cancelBillBtn = QPushButton(self.CartFrame)
        self.cancelBillBtn.setObjectName(u"cancelBillBtn")

        self.gridLayout.addWidget(self.cancelBillBtn, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.cartView = QTableView(self.CartFrame)
        self.cartView.setObjectName(u"cartView")
        self.cartView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cartView.setAlternatingRowColors(True)
        self.cartView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cartView.setShowGrid(True)
        self.cartView.setGridStyle(Qt.SolidLine)
        self.cartView.setSortingEnabled(False)
        self.cartView.setCornerButtonEnabled(True)
        self.cartView.horizontalHeader().setVisible(True)
        self.cartView.horizontalHeader().setStretchLastSection(True)
        self.cartView.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.cartView, 0, 0, 1, 3)


        self.verticalLayout_5.addWidget(self.CartFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.window2ColumnLayoutVertical.addWidget(self.itemAddRow)


        self.Main.addLayout(self.window2ColumnLayoutVertical)


        self.verticalLayout.addLayout(self.Main)

        Dashboard.setCentralWidget(self.dashboardCentralWidget)
        QWidget.setTabOrder(self.Quantity, self.Discount)
        QWidget.setTabOrder(self.Discount, self.addItemBtn)
        QWidget.setTabOrder(self.addItemBtn, self.cancelBtn)
        QWidget.setTabOrder(self.cancelBtn, self.cartView)
        QWidget.setTabOrder(self.cartView, self.Amount)
        QWidget.setTabOrder(self.Amount, self.cgst)
        QWidget.setTabOrder(self.cgst, self.sgst)
        QWidget.setTabOrder(self.sgst, self.igst)
        QWidget.setTabOrder(self.igst, self.totalTax)
        QWidget.setTabOrder(self.totalTax, self.grandTotal)
        QWidget.setTabOrder(self.grandTotal, self.itemNo)
        QWidget.setTabOrder(self.itemNo, self.SalePrice)
        QWidget.setTabOrder(self.SalePrice, self.HSNCode)

        self.retranslateUi(Dashboard)

        self.hamburger.setDefault(False)


        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"LocalShop Connect", None))
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
#if QT_CONFIG(tooltip)
        self.hamburger.setToolTip(QCoreApplication.translate("Dashboard", u"Hide", None))
#endif // QT_CONFIG(tooltip)
        self.hamburger.setText("")
#if QT_CONFIG(tooltip)
        self.billing.setToolTip(QCoreApplication.translate("Dashboard", u"Billing", None))
#endif // QT_CONFIG(tooltip)
        self.billing.setText("")
#if QT_CONFIG(tooltip)
        self.products.setToolTip(QCoreApplication.translate("Dashboard", u"Products", None))
#endif // QT_CONFIG(tooltip)
        self.products.setText("")
#if QT_CONFIG(tooltip)
        self.staff.setToolTip(QCoreApplication.translate("Dashboard", u"Manage Staff", None))
#endif // QT_CONFIG(tooltip)
        self.staff.setText("")
#if QT_CONFIG(shortcut)
        self.staff.setShortcut(QCoreApplication.translate("Dashboard", u"Esc", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.analytics.setToolTip(QCoreApplication.translate("Dashboard", u"Analytics", None))
#endif // QT_CONFIG(tooltip)
        self.analytics.setText("")
#if QT_CONFIG(tooltip)
        self.history.setToolTip(QCoreApplication.translate("Dashboard", u"Bill History", None))
#endif // QT_CONFIG(tooltip)
        self.history.setText("")
#if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate("Dashboard", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings.setText("")
        self.itemNo.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Item No", None))
        self.ProductCode.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Product Code", None))
        self.HSNCode.setPlaceholderText(QCoreApplication.translate("Dashboard", u"HSN Code", None))
        self.SalePrice.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Sale Price", None))
        self.Quantity.setText("")
        self.Quantity.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Quantity", None))
        self.Discount.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Discount", None))
        self.Amount.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Amount", None))
        self.Amount.setProperty("originalValue", "")
        self.cgst.setText("")
        self.cgst.setPlaceholderText(QCoreApplication.translate("Dashboard", u"CGST", None))
        self.sgst.setPlaceholderText(QCoreApplication.translate("Dashboard", u"SGST", None))
        self.igst.setPlaceholderText(QCoreApplication.translate("Dashboard", u"IGST", None))
        self.totalTax.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Total Tax", None))
        self.grandTotal.setText("")
        self.grandTotal.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Grand Total", None))
        self.addItemBtn.setText(QCoreApplication.translate("Dashboard", u"Add Item", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dashboard", u"Cancel Item", None))
        self.confirmBillBtn.setText(QCoreApplication.translate("Dashboard", u"Print Bill", None))
        self.cancelBillBtn.setText(QCoreApplication.translate("Dashboard", u"Cancel Bill", None))
    # retranslateUi

