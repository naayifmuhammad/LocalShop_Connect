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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_AddItem(object):
    def setupUi(self, AddItem):
        if not AddItem.objectName():
            AddItem.setObjectName(u"AddItem")
        AddItem.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/button-icons/plus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        AddItem.setWindowIcon(icon)
        self.actionAdd_new_category = QAction(AddItem)
        self.actionAdd_new_category.setObjectName(u"actionAdd_new_category")
        self.actionRemove_a_category = QAction(AddItem)
        self.actionRemove_a_category.setObjectName(u"actionRemove_a_category")
        self.actionAdd_new_vendor = QAction(AddItem)
        self.actionAdd_new_vendor.setObjectName(u"actionAdd_new_vendor")
        self.actionRemove_existing_vendor = QAction(AddItem)
        self.actionRemove_existing_vendor.setObjectName(u"actionRemove_existing_vendor")
        self.actionView_Vendors = QAction(AddItem)
        self.actionView_Vendors.setObjectName(u"actionView_Vendors")
        self.actionView_Categories = QAction(AddItem)
        self.actionView_Categories.setObjectName(u"actionView_Categories")
        self.actionAdd_Vendors = QAction(AddItem)
        self.actionAdd_Vendors.setObjectName(u"actionAdd_Vendors")
        self.actionRemove_Vendors = QAction(AddItem)
        self.actionRemove_Vendors.setObjectName(u"actionRemove_Vendors")
        self.actionAdd_Categories = QAction(AddItem)
        self.actionAdd_Categories.setObjectName(u"actionAdd_Categories")
        self.actionRemove_Categories = QAction(AddItem)
        self.actionRemove_Categories.setObjectName(u"actionRemove_Categories")
        self.centralwidget = QWidget(AddItem)
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
        self.ItemInfoFrame1 = QFrame(self.frame)
        self.ItemInfoFrame1.setObjectName(u"ItemInfoFrame1")
        self.ItemInfoFrame1.setFrameShape(QFrame.StyledPanel)
        self.ItemInfoFrame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ItemInfoFrame1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.productCode = QLineEdit(self.ItemInfoFrame1)
        self.productCode.setObjectName(u"productCode")
        self.productCode.setProperty("mandatory", True)

        self.verticalLayout_3.addWidget(self.productCode)

        self.vendor = QComboBox(self.ItemInfoFrame1)
        self.vendor.setObjectName(u"vendor")

        self.verticalLayout_3.addWidget(self.vendor)

        self.costPrice = QLineEdit(self.ItemInfoFrame1)
        self.costPrice.setObjectName(u"costPrice")
        self.costPrice.setProperty("mandatory", True)

        self.verticalLayout_3.addWidget(self.costPrice)

        self.taxRate = QLineEdit(self.ItemInfoFrame1)
        self.taxRate.setObjectName(u"taxRate")
        self.taxRate.setProperty("mandatory", True)

        self.verticalLayout_3.addWidget(self.taxRate)

        self.qtyInStock = QLineEdit(self.ItemInfoFrame1)
        self.qtyInStock.setObjectName(u"qtyInStock")
        self.qtyInStock.setProperty("mandatory", False)

        self.verticalLayout_3.addWidget(self.qtyInStock)


        self.horizontalLayout_2.addWidget(self.ItemInfoFrame1)

        self.ItemInfoFrame2 = QFrame(self.frame)
        self.ItemInfoFrame2.setObjectName(u"ItemInfoFrame2")
        self.ItemInfoFrame2.setFrameShape(QFrame.StyledPanel)
        self.ItemInfoFrame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ItemInfoFrame2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.productName = QLineEdit(self.ItemInfoFrame2)
        self.productName.setObjectName(u"productName")
        self.productName.setProperty("mandatory", True)

        self.verticalLayout_2.addWidget(self.productName)

        self.productCategory = QComboBox(self.ItemInfoFrame2)
        self.productCategory.setObjectName(u"productCategory")

        self.verticalLayout_2.addWidget(self.productCategory)

        self.hsnCode = QLineEdit(self.ItemInfoFrame2)
        self.hsnCode.setObjectName(u"hsnCode")
        self.hsnCode.setProperty("mandatory", True)

        self.verticalLayout_2.addWidget(self.hsnCode)

        self.salePrice = QLineEdit(self.ItemInfoFrame2)
        self.salePrice.setObjectName(u"salePrice")
        self.salePrice.setProperty("mandatory", True)

        self.verticalLayout_2.addWidget(self.salePrice)

        self.minStockLevel = QLineEdit(self.ItemInfoFrame2)
        self.minStockLevel.setObjectName(u"minStockLevel")
        self.minStockLevel.setProperty("mandatory", False)

        self.verticalLayout_2.addWidget(self.minStockLevel)


        self.horizontalLayout_2.addWidget(self.ItemInfoFrame2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.Main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.addItem = QPushButton(self.frame_3)
        self.addItem.setObjectName(u"addItem")

        self.horizontalLayout.addWidget(self.addItem)

        self.cancelItem = QPushButton(self.frame_3)
        self.cancelItem.setObjectName(u"cancelItem")

        self.horizontalLayout.addWidget(self.cancelItem)


        self.verticalLayout.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.Main, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        AddItem.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddItem)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuAdd_Remove = QMenu(self.menubar)
        self.menuAdd_Remove.setObjectName(u"menuAdd_Remove")
        self.menuCategories_2 = QMenu(self.menubar)
        self.menuCategories_2.setObjectName(u"menuCategories_2")
        AddItem.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.productCode, self.productName)
        QWidget.setTabOrder(self.productName, self.costPrice)
        QWidget.setTabOrder(self.costPrice, self.hsnCode)
        QWidget.setTabOrder(self.hsnCode, self.taxRate)
        QWidget.setTabOrder(self.taxRate, self.salePrice)
        QWidget.setTabOrder(self.salePrice, self.qtyInStock)
        QWidget.setTabOrder(self.qtyInStock, self.minStockLevel)

        self.menubar.addAction(self.menuAdd_Remove.menuAction())
        self.menubar.addAction(self.menuCategories_2.menuAction())
        self.menuAdd_Remove.addAction(self.actionAdd_Vendors)
        self.menuAdd_Remove.addAction(self.actionRemove_Vendors)
        self.menuCategories_2.addAction(self.actionAdd_Categories)
        self.menuCategories_2.addAction(self.actionRemove_Categories)

        self.retranslateUi(AddItem)

        QMetaObject.connectSlotsByName(AddItem)
    # setupUi

    def retranslateUi(self, AddItem):
        AddItem.setWindowTitle(QCoreApplication.translate("AddItem", u"Add New Item", None))
        self.actionAdd_new_category.setText(QCoreApplication.translate("AddItem", u"Add new category", None))
        self.actionRemove_a_category.setText(QCoreApplication.translate("AddItem", u"Remove a category", None))
        self.actionAdd_new_vendor.setText(QCoreApplication.translate("AddItem", u"Add new vendor", None))
        self.actionRemove_existing_vendor.setText(QCoreApplication.translate("AddItem", u"Remove existing vendor", None))
        self.actionView_Vendors.setText(QCoreApplication.translate("AddItem", u"View Vendors", None))
        self.actionView_Categories.setText(QCoreApplication.translate("AddItem", u"View Categories", None))
        self.actionAdd_Vendors.setText(QCoreApplication.translate("AddItem", u"Add Vendors", None))
        self.actionRemove_Vendors.setText(QCoreApplication.translate("AddItem", u"Remove Vendors", None))
        self.actionAdd_Categories.setText(QCoreApplication.translate("AddItem", u"Add Categories", None))
        self.actionRemove_Categories.setText(QCoreApplication.translate("AddItem", u"Remove Categories", None))
        self.headerLabel.setText(QCoreApplication.translate("AddItem", u"Add New Item", None))
        self.productCode.setPlaceholderText(QCoreApplication.translate("AddItem", u"Product Code *", None))
        self.vendor.setPlaceholderText(QCoreApplication.translate("AddItem", u"Vendor *", None))
        self.costPrice.setPlaceholderText(QCoreApplication.translate("AddItem", u"Cost Price *", None))
        self.taxRate.setPlaceholderText(QCoreApplication.translate("AddItem", u"Tax Rate *", None))
        self.qtyInStock.setPlaceholderText(QCoreApplication.translate("AddItem", u"Qty in Stock", None))
        self.productName.setPlaceholderText(QCoreApplication.translate("AddItem", u"Product Name *", None))
        self.productCategory.setPlaceholderText(QCoreApplication.translate("AddItem", u"Category *", None))
        self.hsnCode.setPlaceholderText(QCoreApplication.translate("AddItem", u"HSN Code *", None))
        self.salePrice.setPlaceholderText(QCoreApplication.translate("AddItem", u"Sale Price *", None))
        self.minStockLevel.setPlaceholderText(QCoreApplication.translate("AddItem", u"Min Stock Level", None))
        self.addItem.setText(QCoreApplication.translate("AddItem", u"Add", None))
        self.cancelItem.setText(QCoreApplication.translate("AddItem", u"Cancel", None))
        self.menuAdd_Remove.setTitle(QCoreApplication.translate("AddItem", u"Vendors", None))
        self.menuCategories_2.setTitle(QCoreApplication.translate("AddItem", u"Categories", None))
    # retranslateUi

