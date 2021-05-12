# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gerha\Google Drive\Studies\Unisa\INF2611 - Visual Programming 2\Programs\INF2611_Python_QT\Assignment1\PRMarketing.ui'
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
        Dialog.resize(497, 473)
        self.labelWelcomeTo = QtGui.QLabel(Dialog)
        self.labelWelcomeTo.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelWelcomeTo.setFont(font)
        self.labelWelcomeTo.setObjectName(_fromUtf8("labelWelcomeTo"))
        self.labelPietRetief = QtGui.QLabel(Dialog)
        self.labelPietRetief.setGeometry(QtCore.QRect(10, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelPietRetief.setFont(font)
        self.labelPietRetief.setObjectName(_fromUtf8("labelPietRetief"))
        self.labelSubscribeTo = QtGui.QLabel(Dialog)
        self.labelSubscribeTo.setGeometry(QtCore.QRect(10, 390, 141, 16))
        self.labelSubscribeTo.setObjectName(_fromUtf8("labelSubscribeTo"))
        self.labelEmail = QtGui.QLabel(Dialog)
        self.labelEmail.setGeometry(QtCore.QRect(10, 410, 31, 16))
        self.labelEmail.setObjectName(_fromUtf8("labelEmail"))
        self.lineEmailAddress = QtGui.QLineEdit(Dialog)
        self.lineEmailAddress.setGeometry(QtCore.QRect(50, 410, 251, 20))
        self.lineEmailAddress.setObjectName(_fromUtf8("lineEmailAddress"))
        self.buttonSubscribe = QtGui.QPushButton(Dialog)
        self.buttonSubscribe.setGeometry(QtCore.QRect(10, 440, 75, 23))
        self.buttonSubscribe.setObjectName(_fromUtf8("buttonSubscribe"))
        self.tabInformation = QtGui.QTabWidget(Dialog)
        self.tabInformation.setGeometry(QtCore.QRect(10, 60, 481, 321))
        self.tabInformation.setObjectName(_fromUtf8("tabInformation"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 481, 301))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabInformation.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 481, 271))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.tabInformation.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 481, 271))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.tabInformation.addTab(self.tab_3, _fromUtf8(""))
        self.labelConfirmation = QtGui.QLabel(Dialog)
        self.labelConfirmation.setGeometry(QtCore.QRect(100, 440, 391, 16))
        self.labelConfirmation.setText(_fromUtf8(""))
        self.labelConfirmation.setObjectName(_fromUtf8("labelConfirmation"))

        self.retranslateUi(Dialog)
        self.tabInformation.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelWelcomeTo.setText(_translate("Dialog", "Welcome To", None))
        self.labelPietRetief.setText(_translate("Dialog", "Piet Retief", None))
        self.labelSubscribeTo.setText(_translate("Dialog", "Subscribe to our news letter", None))
        self.labelEmail.setText(_translate("Dialog", "Email:", None))
        self.buttonSubscribe.setText(_translate("Dialog", "Subscribe", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">About Piet Retief</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic,sans-serif\'; font-size:11pt; font-weight:296; color:#474747; background-color:#ffffff;\">Set in the surrounds of pine forests near one of South Africa’s largest dams you’ll find Piet Retief – the gateway to KwaZulu-Natal Province and Swaziland. Heyshope Dam, found on the Assegaai River and surrounded by pine forests, is one of the biggest dams in the province as well as the country and it’s only 30km away from Piet Retief. Pack a picnic basket, your fishing rods, swimming costume and tents as you head off for a day trip or relaxing weekend break along the water’s edge. With a shoreline of 120km, you’ll surely find a suitable spot to reel in fish. The dam has a reputation as the best place in the country to fish for largemouth bass, but you’ll also find carp and yellowfish in its waters. Locals and seasoned fishermen will tell you to take a boat onto the water if you want to increase your catch. The dam provides a peaceful retreat in nature and is a well-loved place to play sports with your family and friends or settle down with a good book.</span></p></body></html>", None))
        self.tabInformation.setTabText(self.tabInformation.indexOf(self.tab), _translate("Dialog", "About our town", None))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- Fishing - Heyshope Dam</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- Grey Rhebok Hiking Trails</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- Mountain Biking</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- Restaurants</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- Play Golf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.tabInformation.setTabText(self.tabInformation.indexOf(self.tab_2), _translate("Dialog", "Things to do", None))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- LA Guest house</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- Vredenhoff Bed &amp; Breakfast</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- B @ Home Guest House</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- De Loft Guesthouse</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- Welgekozen Country Lodge</span></p></body></html>", None))
        self.tabInformation.setTabText(self.tabInformation.indexOf(self.tab_3), _translate("Dialog", "Where to stay", None))

