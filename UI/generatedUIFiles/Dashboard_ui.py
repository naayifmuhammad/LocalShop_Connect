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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(800, 600)
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
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.MainFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SubFrame = QFrame(self.MainFrame)
        self.SubFrame.setObjectName(u"SubFrame")
        self.SubFrame.setFrameShape(QFrame.StyledPanel)
        self.SubFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.SubFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BIllingFunctions = QGroupBox(self.SubFrame)
        self.BIllingFunctions.setObjectName(u"BIllingFunctions")
        self.BIllingFunctions.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.horizontalLayout = QHBoxLayout(self.BIllingFunctions)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 10, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.BIllingFunctions)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.BIllingFunctions)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.BIllingFunctions)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.BIllingFunctions)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.BIllingFunctions)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.dateEdit = QDateEdit(self.BIllingFunctions)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.label_4 = QLabel(self.BIllingFunctions)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.BIllingFunctions)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.label_5 = QLabel(self.BIllingFunctions)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.BIllingFunctions)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.BIllingFunctions, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.SubFrame, 0, 0, 1, 1)

        self.frame = QFrame(self.MainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 18):
            self.tableWidget.setRowCount(18)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 360))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setBold(True)
        self.label_6.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.MainFrame)

        Dashboard.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Dashboard)
        self.statusbar.setObjectName(u"statusbar")
        Dashboard.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(Dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInventory = QMenu(self.menubar)
        self.menuInventory.setObjectName(u"menuInventory")
        self.menuInventory_2 = QMenu(self.menuInventory)
        self.menuInventory_2.setObjectName(u"menuInventory_2")
        self.menuAdd = QMenu(self.menuInventory_2)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menuModify = QMenu(self.menuInventory_2)
        self.menuModify.setObjectName(u"menuModify")
        self.menuDelete = QMenu(self.menuInventory_2)
        self.menuDelete.setObjectName(u"menuDelete")
        self.menuStaff = QMenu(self.menuInventory)
        self.menuStaff.setObjectName(u"menuStaff")
        Dashboard.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInventory.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionLog_out)
        self.menuInventory.addAction(self.menuInventory_2.menuAction())
        self.menuInventory.addAction(self.menuStaff.menuAction())
        self.menuInventory_2.addAction(self.menuAdd.menuAction())
        self.menuInventory_2.addAction(self.menuModify.menuAction())
        self.menuInventory_2.addAction(self.menuDelete.menuAction())
        self.menuAdd.addAction(self.actionItem)
        self.menuAdd.addAction(self.actionStaff)
        self.menuModify.addAction(self.actionItem_2)
        self.menuModify.addAction(self.actionCategory)
        self.menuDelete.addAction(self.actionItem_3)
        self.menuDelete.addAction(self.actionCategory_2)
        self.menuStaff.addAction(self.actionAdd_Staff)
        self.menuStaff.addAction(self.actionRemove_Staff)

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
        self.BIllingFunctions.setTitle(QCoreApplication.translate("Dashboard", u"Billing Area", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"Staff", None))
        self.label_2.setText(QCoreApplication.translate("Dashboard", u"Bill No", None))
        self.label_3.setText(QCoreApplication.translate("Dashboard", u"Bill Date", None))
        self.label_4.setText(QCoreApplication.translate("Dashboard", u"Customer Name", None))
        self.label_5.setText(QCoreApplication.translate("Dashboard", u"Phone Number", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"Item No", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Qty", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dashboard", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dashboard", u"CGST", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dashboard", u"SGST", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dashboard", u"Discount", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dashboard", u"Total Price", None));
        self.label_7.setText(QCoreApplication.translate("Dashboard", u"Total Price", None))
        self.label_6.setText(QCoreApplication.translate("Dashboard", u"100/-", None))
        self.menuFile.setTitle(QCoreApplication.translate("Dashboard", u"File", None))
        self.menuInventory.setTitle(QCoreApplication.translate("Dashboard", u"Management", None))
        self.menuInventory_2.setTitle(QCoreApplication.translate("Dashboard", u"Inventory", None))
        self.menuAdd.setTitle(QCoreApplication.translate("Dashboard", u"Add", None))
        self.menuModify.setTitle(QCoreApplication.translate("Dashboard", u"Modify", None))
        self.menuDelete.setTitle(QCoreApplication.translate("Dashboard", u"Delete", None))
        self.menuStaff.setTitle(QCoreApplication.translate("Dashboard", u"Staff", None))
    # retranslateUi

