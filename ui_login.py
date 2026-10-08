# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b/Images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 20, 161, 20))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel#label {\n"
"font-family: 'Calibri';\n"
"font-size: 18pt;\n"
"font-weight: bold;\n"
"color: #70B2AF;\n"
"}\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 60, 211, 201))
        self.label_2.setMinimumSize(QSize(150, 150))
        self.label_2.setPixmap(QPixmap(u"../\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b/Images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.ico"))
        self.label_2.setScaledContents(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 330, 221, 43))
        self.layoutWidget.setStyleSheet(u"QLineEDit {\n"
"background-color: #D2F6E7;\n"
"border: 1px solid #70B2AF;\n"
"border-radius: 6px;\n"
"padding: 8px 12px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"color: #333333;\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid #70B2AF;\n"
"background-color: #EAFCF4;\n"
"}\n"
"QLabel {\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"color: #333333;\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loginLabel_2 = QLabel(self.layoutWidget)
        self.loginLabel_2.setObjectName(u"loginLabel_2")
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(12)
        self.loginLabel_2.setFont(font2)
        self.loginLabel_2.setStyleSheet(u"QLabel#lloginLabel_2 {\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}")

        self.horizontalLayout_2.addWidget(self.loginLabel_2)

        self.loginLineEdit_2 = QLineEdit(self.layoutWidget)
        self.loginLineEdit_2.setObjectName(u"loginLineEdit_2")
        self.loginLineEdit_2.setFont(font)
        self.loginLineEdit_2.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.loginLineEdit_2)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(260, 440, 140, 60))
        self.loginButton.setMinimumSize(QSize(140, 60))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.loginButton.setFont(font3)
        self.loginButton.setStyleSheet(u"QPushButton {\n"
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
        self.guestButton = QPushButton(self.centralwidget)
        self.guestButton.setObjectName(u"guestButton")
        self.guestButton.setGeometry(QRect(410, 440, 160, 60))
        self.guestButton.setMinimumSize(QSize(140, 60))
        self.guestButton.setFont(font3)
        self.guestButton.setStyleSheet(u"QPushButton {\n"
"background-color: #D2F6E7;\n"
"color: #333333;\n"
"border: 1px solid #70B2AF;\n"
"border-radius: 6px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#guestButton:hover {\n"
"background-color: #BBEBD7;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f - \u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.label_2.setText("")
        self.loginLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.loginLineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.guestButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434 \u0434\u043b\u044f \u0433\u043e\u0441\u0442\u044f", None))
    # retranslateUi

