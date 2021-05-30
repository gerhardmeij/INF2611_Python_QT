# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gerha\Google Drive\Studies\Unisa\INF2611 - Visual Programming 2\Programs\INF2611_Python_QT\Assignment2\daysToVaccination.ui'
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
        Dialog.resize(603, 331)
        self.headingLable = QtGui.QLabel(Dialog)
        self.headingLable.setGeometry(QtCore.QRect(170, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.headingLable.setFont(font)
        self.headingLable.setObjectName(_fromUtf8("headingLable"))
        self.numberOfDaysLabel = QtGui.QLabel(Dialog)
        self.numberOfDaysLabel.setGeometry(QtCore.QRect(110, 20, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.numberOfDaysLabel.setFont(font)
        self.numberOfDaysLabel.setObjectName(_fromUtf8("numberOfDaysLabel"))
        self.calendarFromWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarFromWidget.setGeometry(QtCore.QRect(10, 120, 280, 155))
        self.calendarFromWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarFromWidget.setObjectName(_fromUtf8("calendarFromWidget"))
        self.calendarToWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarToWidget.setGeometry(QtCore.QRect(310, 120, 280, 155))
        self.calendarToWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarToWidget.setObjectName(_fromUtf8("calendarToWidget"))
        self.currentDateLabel = QtGui.QLabel(Dialog)
        self.currentDateLabel.setGeometry(QtCore.QRect(120, 100, 71, 16))
        self.currentDateLabel.setObjectName(_fromUtf8("currentDateLabel"))
        self.toDateLabel = QtGui.QLabel(Dialog)
        self.toDateLabel.setGeometry(QtCore.QRect(400, 100, 121, 16))
        self.toDateLabel.setObjectName(_fromUtf8("toDateLabel"))
        self.calculateButton = QtGui.QPushButton(Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(270, 290, 61, 23))
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))
        self.curretnDateTimeLabel = QtGui.QLabel(Dialog)
        self.curretnDateTimeLabel.setGeometry(QtCore.QRect(10, 290, 211, 16))
        self.curretnDateTimeLabel.setObjectName(_fromUtf8("curretnDateTimeLabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.headingLable.setText(_translate("Dialog", "Days To Covid19 Vaccination", None))
        self.numberOfDaysLabel.setText(_translate("Dialog", "99", None))
        self.currentDateLabel.setText(_translate("Dialog", "Current Date", None))
        self.toDateLabel.setText(_translate("Dialog", "Select vaccination date", None))
        self.calculateButton.setText(_translate("Dialog", "Calculate", None))
        self.curretnDateTimeLabel.setText(_translate("Dialog", "DateTime", None))

