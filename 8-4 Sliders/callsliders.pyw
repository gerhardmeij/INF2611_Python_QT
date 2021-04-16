import sys 
from slidersdemo import *
class MyForm(QtGui.QDialog): 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        self.ui.horizontalScrollBar.valueChanged.connect(self.scrollhorizontal) 
        self.ui.verticalScrollBar.valueChanged.connect(self.scrollvertical) 
        self.ui.horizontalSlider.valueChanged.connect(self.sliderhorizontal) 
        self.ui.verticalSlider.valueChanged.connect(self.slidervertical)
    def scrollhorizontal(self,value): 
        self.ui.label.setText(str(value)) 
        self.ui.horizontalSlider.setValue(value)
    def scrollvertical(self, value): 
        self.ui.label.setText(str(value)) 
        self.ui.verticalSlider.setValue(value)
    def sliderhorizontal(self, value): 
        self.ui.label.setText(str(value)) 
        self.ui.horizontalScrollBar.setValue(value) 
    def slidervertical(self, value):
        self.ui.label.setText(str(value)) 
        self.ui.verticalScrollBar.setValue(value)

if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv) 
    myapp = MyForm() 
    myapp.show() 
    sys.exit(app.exec_())