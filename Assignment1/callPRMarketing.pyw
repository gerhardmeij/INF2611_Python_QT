import sys 
from PRMarketing import *

class MyForm(QtGui.QDialog): 
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        QtCore.QObject.connect(self.ui.buttonSubscribe, QtCore.SIGNAL('clicked()'),self.confirmSubscribe)

    def confirmSubscribe(self): 
        email=self.ui.lineEmailAddress.text() 
        self.ui.labelConfirmation.setText('Thank you, '+str(email)+' is now subscribed!')

if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv) 
    myapp = MyForm() 
    myapp.show() 
    sys.exit(app.exec_())