# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddCategories.ui'
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

class Ui_AddCategory(object):
    def setupUi(self, AddCategory):
        if not AddCategory.objectName():
            AddCategory.setObjectName(u"AddCategory")
        AddCategory.resize(803, 585)
        icon = QIcon()
        icon.addFile(u":/button-icons/plus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        AddCategory.setWindowIcon(icon)
        self.actionAdd_new_category = QAction(AddCategory)
        self.actionAdd_new_category.setObjectName(u"actionAdd_new_category")
        self.actionRemove_a_category = QAction(AddCategory)
        self.actionRemove_a_category.setObjectName(u"actionRemove_a_category")
        self.actionAdd_new_vendor = QAction(AddCategory)
        self.actionAdd_new_vendor.setObjectName(u"actionAdd_new_vendor")
        self.actionRemove_existing_vendor = QAction(AddCategory)
        self.actionRemove_existing_vendor.setObjectName(u"actionRemove_existing_vendor")
        self.actionView_Vendors = QAction(AddCategory)
        self.actionView_Vendors.setObjectName(u"actionView_Vendors")
        self.actionView_Categories = QAction(AddCategory)
        self.actionView_Categories.setObjectName(u"actionView_Categories")
        self.actionAdd_Vendors = QAction(AddCategory)
        self.actionAdd_Vendors.setObjectName(u"actionAdd_Vendors")
        self.actionRemove_Vendors = QAction(AddCategory)
        self.actionRemove_Vendors.setObjectName(u"actionRemove_Vendors")
        self.actionAdd_Categories = QAction(AddCategory)
        self.actionAdd_Categories.setObjectName(u"actionAdd_Categories")
        self.actionRemove_Categories = QAction(AddCategory)
        self.actionRemove_Categories.setObjectName(u"actionRemove_Categories")
        self.centralwidget = QWidget(AddCategory)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.Main = QFrame(self.centralwidget)
        self.Main.setObjectName(u"Main")
        self.Main.setMinimumSize(QSize(596, 400))
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

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
        self.name = QLineEdit(self.InputFields)
        self.name.setObjectName(u"name")
        self.name.setProperty("mandatory", True)

        self.verticalLayout_3.addWidget(self.name)

        self.description = QLineEdit(self.InputFields)
        self.description.setObjectName(u"description")
        self.description.setProperty("mandatory", False)

        self.verticalLayout_3.addWidget(self.description)


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


        self.gridLayout.addWidget(self.Main, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        AddCategory.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.name, self.description)

        self.retranslateUi(AddCategory)

        QMetaObject.connectSlotsByName(AddCategory)
    # setupUi

    def retranslateUi(self, AddCategory):
        AddCategory.setWindowTitle(QCoreApplication.translate("AddCategory", u"Add Vendor", None))
        self.actionAdd_new_category.setText(QCoreApplication.translate("AddCategory", u"Add new category", None))
        self.actionRemove_a_category.setText(QCoreApplication.translate("AddCategory", u"Remove a category", None))
        self.actionAdd_new_vendor.setText(QCoreApplication.translate("AddCategory", u"Add new vendor", None))
        self.actionRemove_existing_vendor.setText(QCoreApplication.translate("AddCategory", u"Remove existing vendor", None))
        self.actionView_Vendors.setText(QCoreApplication.translate("AddCategory", u"View Vendors", None))
        self.actionView_Categories.setText(QCoreApplication.translate("AddCategory", u"View Categories", None))
        self.actionAdd_Vendors.setText(QCoreApplication.translate("AddCategory", u"Add Vendors", None))
        self.actionRemove_Vendors.setText(QCoreApplication.translate("AddCategory", u"Remove Vendors", None))
        self.actionAdd_Categories.setText(QCoreApplication.translate("AddCategory", u"Add Categories", None))
        self.actionRemove_Categories.setText(QCoreApplication.translate("AddCategory", u"Remove Categories", None))
        self.headerLabel.setText(QCoreApplication.translate("AddCategory", u"Add Category", None))
        self.name.setPlaceholderText(QCoreApplication.translate("AddCategory", u"Category Name *", None))
        self.description.setPlaceholderText(QCoreApplication.translate("AddCategory", u"Description", None))
        self.add.setText(QCoreApplication.translate("AddCategory", u"Add", None))
        self.cancel.setText(QCoreApplication.translate("AddCategory", u"Cancel", None))
    # retranslateUi

