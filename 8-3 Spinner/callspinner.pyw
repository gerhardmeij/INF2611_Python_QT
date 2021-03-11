import sys 
from spinner import *

class MyForm(QtGui.QDialog): 
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        QtCore.QObject.connect(self.ui.spinBox, QtCore.SIGNAL('editingFinished()'),self.result1) 
        QtCore.QObject.connect(self.ui.doubleSpinBox, QtCore.SIGNAL('editingFinished()'), self.result2) 
        QtCore.QObject.connect(self.ui.AddButton, QtCore.SIGNAL('clicked()'),self.addvalues)
    def result1(self): 
        self.ui.lineFirstValue.setText(str(self.ui.spinBox.value()))

    def result2(self): 
        self.ui.lineSecondValue.setText(str(self.ui.doubleSpinBox.value()))

    def addvalues(self): 
        sum=self.ui.spinBox.value()+self.ui.doubleSpinBox.value() 
        self.ui.labelAddition.setText('Sum is '+str(sum))

if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv) 
    myapp = MyForm() 
    myapp.show() 
    sys.exit(app.exec_())