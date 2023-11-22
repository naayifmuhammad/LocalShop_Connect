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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.ItemDetails = QTableWidget(self.itemAddRow)
        if (self.ItemDetails.columnCount() < 7):
            self.ItemDetails.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.ItemDetails.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ItemDetails.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ItemDetails.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ItemDetails.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ItemDetails.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ItemDetails.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ItemDetails.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.ItemDetails.rowCount() < 1):
            self.ItemDetails.setRowCount(1)
        self.ItemDetails.setObjectName(u"ItemDetails")
        self.ItemDetails.setMaximumSize(QSize(16777215, 70))
        self.ItemDetails.setFrameShadow(QFrame.Plain)
        self.ItemDetails.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ItemDetails.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.ItemDetails.setProperty("showDropIndicator", True)
        self.ItemDetails.setAlternatingRowColors(True)
        self.ItemDetails.setShowGrid(False)
        self.ItemDetails.horizontalHeader().setVisible(True)
        self.ItemDetails.horizontalHeader().setMinimumSectionSize(32)
        self.ItemDetails.horizontalHeader().setHighlightSections(True)
        self.ItemDetails.horizontalHeader().setStretchLastSection(True)
        self.ItemDetails.verticalHeader().setVisible(False)
        self.ItemDetails.verticalHeader().setMinimumSectionSize(0)
        self.ItemDetails.verticalHeader().setDefaultSectionSize(31)
        self.ItemDetails.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.ItemDetails)

        self.taxDetails = QTableWidget(self.itemAddRow)
        if (self.taxDetails.columnCount() < 5):
            self.taxDetails.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.taxDetails.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.taxDetails.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.taxDetails.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.taxDetails.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.taxDetails.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        if (self.taxDetails.rowCount() < 1):
            self.taxDetails.setRowCount(1)
        self.taxDetails.setObjectName(u"taxDetails")
        self.taxDetails.setMaximumSize(QSize(16777215, 70))
        self.taxDetails.setFrameShadow(QFrame.Plain)
        self.taxDetails.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.taxDetails.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.taxDetails.setProperty("showDropIndicator", True)
        self.taxDetails.setAlternatingRowColors(False)
        self.taxDetails.setShowGrid(False)
        self.taxDetails.horizontalHeader().setMinimumSectionSize(32)
        self.taxDetails.horizontalHeader().setStretchLastSection(True)
        self.taxDetails.verticalHeader().setVisible(False)
        self.taxDetails.verticalHeader().setMinimumSectionSize(0)
        self.taxDetails.verticalHeader().setDefaultSectionSize(31)
        self.taxDetails.verticalHeader().setStretchLastSection(False)

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

        self.closeBtn = QPushButton(self.confirmAddItemFrame)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout.addWidget(self.closeBtn)


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
        self.cartView.setShowGrid(False)
        self.cartView.setGridStyle(Qt.NoPen)
        self.cartView.setSortingEnabled(True)
        self.cartView.setCornerButtonEnabled(False)
        self.cartView.horizontalHeader().setVisible(True)
        self.cartView.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.cartView, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.CartFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.window2ColumnLayoutVertical.addWidget(self.itemAddRow)


        self.mainLayout.addLayout(self.window2ColumnLayoutVertical, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.mainLayout)

        Dashboard.setCentralWidget(self.dashboardCentralWidget)

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
        ___qtablewidgetitem = self.ItemDetails.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"itemNo", None));
        ___qtablewidgetitem1 = self.ItemDetails.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Product ID", None));
        ___qtablewidgetitem2 = self.ItemDetails.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dashboard", u"HSN Code", None));
        ___qtablewidgetitem3 = self.ItemDetails.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dashboard", u"Sale Price", None));
        ___qtablewidgetitem4 = self.ItemDetails.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dashboard", u"Qty", None));
        ___qtablewidgetitem5 = self.ItemDetails.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dashboard", u"Discount", None));
        ___qtablewidgetitem6 = self.ItemDetails.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dashboard", u"Amount", None));
        ___qtablewidgetitem7 = self.taxDetails.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dashboard", u"CSGT", None));
        ___qtablewidgetitem8 = self.taxDetails.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dashboard", u"SGST", None));
        ___qtablewidgetitem9 = self.taxDetails.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dashboard", u"IGST", None));
        ___qtablewidgetitem10 = self.taxDetails.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dashboard", u"Total tax", None));
        ___qtablewidgetitem11 = self.taxDetails.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dashboard", u"Final Amount", None));
        self.addItemBtn.setText(QCoreApplication.translate("Dashboard", u"Add Item", None))
        self.closeBtn.setText(QCoreApplication.translate("Dashboard", u"Cancel Item", None))
    # retranslateUi

