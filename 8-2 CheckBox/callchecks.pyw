import sys 
from checkbx import *

class MyForm(QtGui.QDialog): 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        QtCore.QObject.connect(self.ui.CalculateButton, QtCore.SIGNAL('clicked()'),self.calculate)
    def calculate(self): 
        amt=0 
        if self.ui.checkPizza20.isChecked()==True: 
            amt=amt+20
        if self.ui.checkHotDog5.isChecked()==True: 
            amt=amt+5
        if self.ui.checkFries10.isChecked()==True: 
            amt=amt+10
        if self.ui.checkBurger15.isChecked()==True: 
            amt=amt+15 
        self.ui.lineAmount.setText(str(amt))

if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv) 
    myapp = MyForm() 
    myapp.show() 
    sys.exit(app.exec_())