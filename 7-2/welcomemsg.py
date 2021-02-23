# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gerha\Google Drive\Studies\Unisa\INF2611 - Visual Programming 2\Programs\7-2\welcomemsg.ui'
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
        self.labelEnterName = QtGui.QLabel(Dialog)
        self.labelEnterName.setGeometry(QtCore.QRect(80, 90, 46, 13))
        self.labelEnterName.setObjectName(_fromUtf8("labelEnterName"))
        self.labelMessage = QtGui.QLabel(Dialog)
        self.labelMessage.setGeometry(QtCore.QRect(160, 160, 46, 13))
        self.labelMessage.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelMessage.setText(_fromUtf8(""))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.lineUserName = QtGui.QLineEdit(Dialog)
        self.lineUserName.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.lineUserName.setObjectName(_fromUtf8("lineUserName"))
        self.clickMeButton = QtGui.QPushButton(Dialog)
        self.clickMeButton.setGeometry(QtCore.QRect(140, 220, 75, 23))
        self.clickMeButton.setObjectName(_fromUtf8("clickMeButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelEnterName.setText(_translate("Dialog", "Enter your name", None))
        self.clickMeButton.setText(_translate("Dialog", "Click Me", None))

