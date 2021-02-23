# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gerha\Google Drive\Studies\Unisa\INF2611 - Visual Programming 2\Programs\7-3\addtwonum.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.labelFirstNumber = QtGui.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(30, 60, 46, 13))
        self.labelFirstNumber.setObjectName(_fromUtf8("labelFirstNumber"))
        self.labelSecondNumber = QtGui.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.labelSecondNumber.setObjectName(_fromUtf8("labelSecondNumber"))
        self.labelAddition = QtGui.QLabel(Dialog)
        self.labelAddition.setGeometry(QtCore.QRect(90, 160, 271, 16))
        self.labelAddition.setObjectName(_fromUtf8("labelAddition"))
        self.lineFirstNumber = QtGui.QLineEdit(Dialog)
        self.lineFirstNumber.setGeometry(QtCore.QRect(140, 60, 201, 20))
        self.lineFirstNumber.setObjectName(_fromUtf8("lineFirstNumber"))
        self.lineSecondNumber = QtGui.QLineEdit(Dialog)
        self.lineSecondNumber.setGeometry(QtCore.QRect(140, 100, 201, 20))
        self.lineSecondNumber.setObjectName(_fromUtf8("lineSecondNumber"))
        self.AddButton = QtGui.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.AddButton.setObjectName(_fromUtf8("AddButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number", None))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number", None))
        self.labelAddition.setText(_translate("Dialog", "TextLabel", None))
        self.AddButton.setText(_translate("Dialog", "Add", None))

