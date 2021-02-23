import sys 
from welcomemsg import * 
class MyForm(QtGui.QDialog):
 def __init__(self, parent=None):
  QtGui.QWidget.__init__(self, parent)
  self.ui = Ui_Dialog() 
  self.ui.setupUi(self) 
  QtCore.QObject.connect(self.ui.clickMeButton, QtCore.SIGNAL('clicked()'),self.dispmessage)

 def dispmessage(self): 
  self.ui.labelMessage.setText("Hello "+ self.ui.lineUserName.text())

  
if __name__ == "__main__":
 app = QtGui.QApplication(sys.argv)
 myapp = MyForm()
 myapp.show()
 sys.exit(app.exec_())