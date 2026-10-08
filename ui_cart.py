# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cart.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CartDialog(object):
    def setupUi(self, CartDialog):
        if not CartDialog.objectName():
            CartDialog.setObjectName(u"CartDialog")
        CartDialog.resize(800, 600)
        CartDialog.setMinimumSize(QSize(800, 600))
        CartDialog.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"programming_course-main/\u041f\u0440\u0438\u043b_2_\u041e\u0417_\u041a\u0418\u041c_09.02.07-2-2027/Images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.png", QSize(), QIcon.Normal, QIcon.Off)
        CartDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(CartDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logoLabel = QLabel(CartDialog)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMaximumSize(QSize(64, 64))
        self.logoLabel.setPixmap(QPixmap(u"../\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b/Images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.ico"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logoLabel)

        self.horizontalSpacer_2 = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.titleLabel = QLabel(CartDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"QLabel#titleLabel {\n"
"font-family: 'Calibri';\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"color: #70B2AF;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.titleLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.cartTable = QTableWidget(CartDialog)
        self.cartTable.setObjectName(u"cartTable")

        self.verticalLayout.addWidget(self.cartTable)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(98, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.totalPriceLabel = QLabel(CartDialog)
        self.totalPriceLabel.setObjectName(u"totalPriceLabel")
        self.totalPriceLabel.setStyleSheet(u"QLabel#totalPriceLabel {\n"
"font-family: 'Calibri';\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.totalPriceLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.removeItemButton = QPushButton(CartDialog)
        self.removeItemButton.setObjectName(u"removeItemButton")
        self.removeItemButton.setStyleSheet(u"QPushButton#removeItemButton{\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"background-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.removeItemButton)

        self.clearCartButton = QPushButton(CartDialog)
        self.clearCartButton.setObjectName(u"clearCartButton")
        self.clearCartButton.setStyleSheet(u"QPushButton#clearCartButton{\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"background-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.clearCartButton)

        self.checkoutButton = QPushButton(CartDialog)
        self.checkoutButton.setObjectName(u"checkoutButton")
        self.checkoutButton.setStyleSheet(u"QPushButton#\u0441heckoutButton{\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"background-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.checkoutButton)

        self.backButton = QPushButton(CartDialog)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setStyleSheet(u"QPushButton#backButton{\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"background-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.backButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CartDialog)

        QMetaObject.connectSlotsByName(CartDialog)
    # setupUi

    def retranslateUi(self, CartDialog):
        CartDialog.setWindowTitle(QCoreApplication.translate("CartDialog", u"Form", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("CartDialog", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430 \u0438 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.totalPriceLabel.setText(QCoreApplication.translate("CartDialog", u"\u0418\u0442\u043e\u0433\u043e \u043a \u043e\u043f\u043b\u0430\u0442\u0435: 0.00 \u0440\u0443\u0431.", None))
        self.removeItemButton.setText(QCoreApplication.translate("CartDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 \u043a\u043e\u0440\u0437\u0438\u043d\u044b", None))
        self.clearCartButton.setText(QCoreApplication.translate("CartDialog", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.checkoutButton.setText(QCoreApplication.translate("CartDialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.backButton.setText(QCoreApplication.translate("CartDialog", u"\u041d\u0430\u0437\u0430\u0434 \u0432 \u043a\u0430\u0442\u0430\u043b\u043e\u0433", None))
    # retranslateUi

