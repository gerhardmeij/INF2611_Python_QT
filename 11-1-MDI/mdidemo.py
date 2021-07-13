# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gerha\Google Drive\Studies\Unisa\INF2611 - Visual Programming 2\Programs\INF2611_Python_QT\11-1-MDI\mdidemo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.subwindow = QtGui.QWidget()
        self.subwindow.setObjectName(_fromUtf8("subwindow"))
        self.pushButton = QtGui.QPushButton(self.subwindow)
        self.pushButton.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.subwindow_2 = QtGui.QWidget()
        self.subwindow_2.setObjectName(_fromUtf8("subwindow_2"))
        self.pushButton_2 = QtGui.QPushButton(self.subwindow_2)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 220, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.showNext = QtGui.QPushButton(self.centralwidget)
        self.showNext.setGeometry(QtCore.QRect(30, 490, 75, 23))
        self.showNext.setObjectName(_fromUtf8("showNext"))
        self.showPrevious = QtGui.QPushButton(self.centralwidget)
        self.showPrevious.setGeometry(QtCore.QRect(110, 490, 91, 23))
        self.showPrevious.setObjectName(_fromUtf8("showPrevious"))
        self.closeAll = QtGui.QPushButton(self.centralwidget)
        self.closeAll.setGeometry(QtCore.QRect(210, 490, 75, 23))
        self.closeAll.setObjectName(_fromUtf8("closeAll"))
        self.cascadeButton = QtGui.QPushButton(self.centralwidget)
        self.cascadeButton.setGeometry(QtCore.QRect(300, 490, 75, 23))
        self.cascadeButton.setObjectName(_fromUtf8("cascadeButton"))
        self.tileButton = QtGui.QPushButton(self.centralwidget)
        self.tileButton.setGeometry(QtCore.QRect(390, 490, 75, 23))
        self.tileButton.setObjectName(_fromUtf8("tileButton"))
        self.SubWindowViewButton = QtGui.QPushButton(self.centralwidget)
        self.SubWindowViewButton.setGeometry(QtCore.QRect(480, 490, 101, 23))
        self.SubWindowViewButton.setObjectName(_fromUtf8("SubWindowViewButton"))
        self.TabbedViewButton = QtGui.QPushButton(self.centralwidget)
        self.TabbedViewButton.setGeometry(QtCore.QRect(590, 490, 75, 23))
        self.TabbedViewButton.setObjectName(_fromUtf8("TabbedViewButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFirst_Window = QtGui.QAction(MainWindow)
        self.actionFirst_Window.setObjectName(_fromUtf8("actionFirst_Window"))
        self.actionSecond_Window = QtGui.QAction(MainWindow)
        self.actionSecond_Window.setObjectName(_fromUtf8("actionSecond_Window"))
        self.menuWindows.addSeparator()
        self.menuWindows.addAction(self.actionFirst_Window)
        self.menuWindows.addAction(self.actionSecond_Window)
        self.menubar.addAction(self.menuWindows.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.subwindow.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.pushButton.setText(_translate("MainWindow", "Sub 1", None))
        self.subwindow_2.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Sub2", None))
        self.showNext.setText(_translate("MainWindow", "Show Next", None))
        self.showPrevious.setText(_translate("MainWindow", "Show Previous", None))
        self.closeAll.setText(_translate("MainWindow", "Close All", None))
        self.cascadeButton.setText(_translate("MainWindow", "Cascade", None))
        self.tileButton.setText(_translate("MainWindow", "Tile", None))
        self.SubWindowViewButton.setText(_translate("MainWindow", "Sub Window View", None))
        self.TabbedViewButton.setText(_translate("MainWindow", "Tabbed View", None))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows", None))
        self.actionFirst_Window.setText(_translate("MainWindow", "First Window", None))
        self.actionSecond_Window.setText(_translate("MainWindow", "Second Window", None))

