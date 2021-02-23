# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gerha\Google Drive\Studies\Unisa\INF2611 - Visual Programming 2\Programs\7-4  Buddies\buddies.ui'
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
        Dialog.resize(269, 277)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 180, 111, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.quantity = QtGui.QLineEdit(Dialog)
        self.quantity.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.quantity.setObjectName(_fromUtf8("quantity"))
        self.rate = QtGui.QLineEdit(Dialog)
        self.rate.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.rate.setObjectName(_fromUtf8("rate"))
        self.discount = QtGui.QLineEdit(Dialog)
        self.discount.setGeometry(QtCore.QRect(140, 140, 113, 20))
        self.discount.setObjectName(_fromUtf8("discount"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.result = QtGui.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(30, 240, 191, 16))
        self.result.setObjectName(_fromUtf8("result"))
        self.label.setBuddy(self.quantity)
        self.label_2.setBuddy(self.rate)
        self.label_3.setBuddy(self.discount)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.quantity, self.rate)
        Dialog.setTabOrder(self.rate, self.discount)
        Dialog.setTabOrder(self.discount, self.pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Calculate Amount", None))
        self.label.setText(_translate("Dialog", "&Number of items", None))
        self.label_2.setText(_translate("Dialog", "&Price per item", None))
        self.label_3.setText(_translate("Dialog", "&Discount Percentage", None))
        self.result.setText(_translate("Dialog", "TextLabel", None))

