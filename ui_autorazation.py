# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autorazation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMaximumSize(QSize(64, 64))
        self.logoLabel.setPixmap(QPixmap(u"../\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b/Images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.ico"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logoLabel)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"QLabel#titleLabel {\n"
"font-family: 'Calibri';\n"
"font-size: 18pt;\n"
"font-weight: bold;\n"
"color: #70B2AF;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.userinfolabel = QLabel(self.centralwidget)
        self.userinfolabel.setObjectName(u"userinfolabel")
        self.userinfolabel.setStyleSheet(u"QLabel#userinfolabel {\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}")

        self.horizontalLayout.addWidget(self.userinfolabel)

        self.LogoutButton = QPushButton(self.centralwidget)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setStyleSheet(u"QPushButton {\n"
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
"back-ground-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}")

        self.horizontalLayout.addWidget(self.LogoutButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchLineEdit = QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setStyleSheet(u"QLineEdit#searchLineEdit {\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.searchLineEdit)

        self.filterComboBox = QComboBox(self.centralwidget)
        self.filterComboBox.setObjectName(u"filterComboBox")
        self.filterComboBox.setStyleSheet(u"QComboBox#filterComboBox{\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"background-color: #70B2AF\n"
"}")

        self.horizontalLayout_2.addWidget(self.filterComboBox)

        self.sortComboBox = QComboBox(self.centralwidget)
        self.sortComboBox.setObjectName(u"sortComboBox")
        self.sortComboBox.setStyleSheet(u"QComboBox#sortComboBox{\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"background-color: #70B2AF\n"
"}")

        self.horizontalLayout_2.addWidget(self.sortComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.productsTable = QTableWidget(self.centralwidget)
        self.productsTable.setObjectName(u"productsTable")

        self.verticalLayout.addWidget(self.productsTable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(358, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.addToOrderButton = QPushButton(self.centralwidget)
        self.addToOrderButton.setObjectName(u"addToOrderButton")
        self.addToOrderButton.setStyleSheet(u"QPushButton#addToOrderButton{\n"
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
"back-ground-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.addToOrderButton)

        self.manageOrdersButton = QPushButton(self.centralwidget)
        self.manageOrdersButton.setObjectName(u"manageOrdersButton")
        self.manageOrdersButton.setStyleSheet(u"QPushButton#manageOrdersButton{\n"
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
"back-ground-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.manageOrdersButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
        self.userinfolabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.searchLineEdit.setText("")
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.addToOrderButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437/\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.manageOrdersButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430\u043c\u0438", None))
    # retranslateUi

