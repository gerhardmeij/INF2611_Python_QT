from __future__ import division 
import sys 
from buddies import *
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
          QtGui.QWidget.__init__(self, parent)
          self.ui = Ui_Dialog() 
          self.ui.setupUi(self) 
          QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.calculate)
    def calculate(self):
        if len(self.ui.quantity.text())!=0: q=int(self.ui.quantity.text())
        else: q=0
        if len(self.ui.rate.text())!=0: r=int(self.ui.rate.text())
        else: r=0
        if len(self.ui.discount.text())!=0: d=int(self.ui.discount.text())
        else: d=0
        totamt=q*r
        disc=totamt*d/100 
        netamt=totamt-disc 
        self.ui.result.setText("Total Amount: " +str(totamt)+", Discount: "+str(disc)+" , Net Amount: "+str(netamt))

if __name__ == "__main__":
     app = QtGui.QApplication(sys.argv) 
     myapp = MyForm() 
     myapp.show() 
     sys.exit(app.exec_())