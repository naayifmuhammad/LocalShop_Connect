# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUp.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_PopUp(object):
    def setupUi(self, PopUp):
        if not PopUp.objectName():
            PopUp.setObjectName(u"PopUp")
        PopUp.resize(500, 250)
        PopUp.setMinimumSize(QSize(0, 0))
        PopUp.setMaximumSize(QSize(16777215, 16777215))
        PopUp.setBaseSize(QSize(500, 250))
        self.PopUpCentralWidget = QWidget(PopUp)
        self.PopUpCentralWidget.setObjectName(u"PopUpCentralWidget")
        self.gridLayout_2 = QGridLayout(self.PopUpCentralWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_msg = QLabel(self.PopUpCentralWidget)
        self.label_msg.setObjectName(u"label_msg")
        self.label_msg.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Reem Kufi"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_msg.setFont(font)
        self.label_msg.setAlignment(Qt.AlignCenter)
        self.label_msg.setWordWrap(True)

        self.gridLayout.addWidget(self.label_msg, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.customTitleSlot = QVBoxLayout()
        self.customTitleSlot.setObjectName(u"customTitleSlot")

        self.gridLayout_2.addLayout(self.customTitleSlot, 0, 0, 1, 1)

        PopUp.setCentralWidget(self.PopUpCentralWidget)

        self.retranslateUi(PopUp)

        QMetaObject.connectSlotsByName(PopUp)
    # setupUi

    def retranslateUi(self, PopUp):
        PopUp.setWindowTitle(QCoreApplication.translate("PopUp", u"Alert", None))
        self.label_msg.setText(QCoreApplication.translate("PopUp", u"Registeration was successfully completed you know", None))
    # retranslateUi

