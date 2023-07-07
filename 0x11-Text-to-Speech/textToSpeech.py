# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textToSpeech.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-image:url(:/newPrefix/bg.jpg);\n"
"background-position:center bottom;\n"
"background-repeat:no-repeat;\n"
"background-attachment:fixed;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appTitle = QtWidgets.QLabel(self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(180, 30, 261, 71))
        self.appTitle.setStyleSheet("font-family:calibri;\n"
"font-size:28px;\n"
"font-weight: bold; \n"
"color:white;\n"
"background:transparent;")
        self.appTitle.setObjectName("appTitle")
        self.textTitle = QtWidgets.QLabel(self.centralwidget)
        self.textTitle.setGeometry(QtCore.QRect(140, 110, 311, 71))
        self.textTitle.setStyleSheet("font-family:calibri;\n"
"font-size:20px;\n"
"font-weight: bold; \n"
"color:white;\n"
"background:transparent;")
        self.textTitle.setObjectName("textTitle")
        self.textArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textArea.setGeometry(QtCore.QRect(110, 200, 361, 96))
        self.textArea.setStyleSheet("font-family:calibri;\n"
"padding: 8px;\n"
"color:orange;\n"
"font-size:20px;\n"
"border-radius:12px;\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"border:solid 2px white")
        self.textArea.setPlainText("")
        self.textArea.setObjectName("textArea")
        self.convertBtn = KPushButton(self.centralwidget)
        self.convertBtn.setGeometry(QtCore.QRect(150, 330, 281, 28))
        self.convertBtn.setStyleSheet("background:transparent; \n"
"background-color:orange; \n"
"font-weight:bold; \n"
"font-size:18px;\n"
"color:white;\n"
"")
        self.convertBtn.setObjectName("convertBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "textTo Speech"))
        self.appTitle.setText(_translate("MainWindow", "Text To Speech"))
        self.textTitle.setText(_translate("MainWindow", "  Write Or Paste Your Text "))
## from kpushbutton import KPushButton
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())