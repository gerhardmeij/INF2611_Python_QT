# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gerha\Google Drive\Studies\Unisa\INF2611 - Visual Programming 2\Programs\INF2611_Python_QT\8-1 RadioMuttonCalculator\radiobtn.ui'
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
        self.labelFirstNumber.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.labelFirstNumber.setObjectName(_fromUtf8("labelFirstNumber"))
        self.labelSecondNumber = QtGui.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.labelSecondNumber.setObjectName(_fromUtf8("labelSecondNumber"))
        self.lineFirstNumber = QtGui.QLineEdit(Dialog)
        self.lineFirstNumber.setGeometry(QtCore.QRect(160, 30, 113, 20))
        self.lineFirstNumber.setObjectName(_fromUtf8("lineFirstNumber"))
        self.lineSecondNumber = QtGui.QLineEdit(Dialog)
        self.lineSecondNumber.setGeometry(QtCore.QRect(160, 60, 113, 20))
        self.lineSecondNumber.setObjectName(_fromUtf8("lineSecondNumber"))
        self.ComputeButton = QtGui.QPushButton(Dialog)
        self.ComputeButton.setGeometry(QtCore.QRect(250, 250, 75, 23))
        self.ComputeButton.setObjectName(_fromUtf8("ComputeButton"))
        self.labelResult = QtGui.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(40, 220, 46, 13))
        self.labelResult.setObjectName(_fromUtf8("labelResult"))
        self.radioAdd = QtGui.QRadioButton(Dialog)
        self.radioAdd.setGeometry(QtCore.QRect(30, 100, 82, 17))
        self.radioAdd.setObjectName(_fromUtf8("radioAdd"))
        self.radioSubtract = QtGui.QRadioButton(Dialog)
        self.radioSubtract.setGeometry(QtCore.QRect(30, 120, 82, 17))
        self.radioSubtract.setObjectName(_fromUtf8("radioSubtract"))
        self.radioMultiply = QtGui.QRadioButton(Dialog)
        self.radioMultiply.setGeometry(QtCore.QRect(30, 140, 82, 17))
        self.radioMultiply.setObjectName(_fromUtf8("radioMultiply"))
        self.radioDivide = QtGui.QRadioButton(Dialog)
        self.radioDivide.setGeometry(QtCore.QRect(30, 160, 82, 17))
        self.radioDivide.setObjectName(_fromUtf8("radioDivide"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number", None))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number", None))
        self.ComputeButton.setText(_translate("Dialog", "Compute", None))
        self.labelResult.setText(_translate("Dialog", "TextLabel", None))
        self.radioAdd.setText(_translate("Dialog", "Add", None))
        self.radioSubtract.setText(_translate("Dialog", "Subtract", None))
        self.radioMultiply.setText(_translate("Dialog", "Multiply", None))
        self.radioDivide.setText(_translate("Dialog", "Divide", None))

