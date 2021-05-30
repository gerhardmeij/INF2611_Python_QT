import sys 
from daysToVaccination import *
class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
          QtGui.QWidget.__init__(self, parent) 
          self.ui = Ui_Dialog() 
          self.ui.setupUi(self) 
          timer = QtCore.QTimer(self) 
          timer.timeout.connect(self.showlcd) 
          timer.start(1000)

          self.ui.calendarFromWidget.showToday()
          self.ui.calendarToWidget.showToday()
          QtCore.QObject.connect(self.ui.calculateButton, QtCore.SIGNAL('clicked()'), self.calcDate)

    def calcDate(self):
         daysToVaccination = QtCore.QDate.daysTo(self.ui.calendarFromWidget.selectedDate(), self.ui.calendarToWidget.selectedDate())
         self.ui.numberOfDaysLabel.setText(str(daysToVaccination))

    def showlcd(self):
         date = QtCore.QDate.currentDate()
         time = QtCore.QTime.currentTime() 
         timeText = time.toString('hh:mm:ss') 
         dateText = date.toPyDate()
         self.ui.curretnDateTimeLabel.setText(str(dateText) + " "+ str(timeText))
         
if __name__ == "__main__":
     app = QtGui.QApplication(sys.argv) 
     myapp = MyForm() 
     myapp.show() 
     sys.exit(app.exec_())