import sys 
from EventMan import *
class MyForm(QtGui.QMainWindow): 
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self) 
        self.connect(self.ui.actionAdd_Event, QtCore.SIGNAL('triggered()'),self.displayAddEvent) 
        self.connect(self.ui.actionNew_Client, QtCore.SIGNAL('triggered()'),self.displayAddClient)
        self.connect(self.ui.actionNew_Venue, QtCore.SIGNAL('triggered()'),self.displayAddVenue)
        self.connect(self.ui.actionAll_Events, QtCore.SIGNAL('triggered()'),self.displayAllEvents)
        self.connect(self.ui.actionAll_Clients, QtCore.SIGNAL('triggered()'),self.displayAllClients)
        self.connect(self.ui.actionAll_Venues, QtCore.SIGNAL('triggered()'),self.displayAllVenues)

    def displayAddEvent(self): 
        self.ui.mdiArea.addSubWindow(self.ui.AddEvent) 
        self.ui.AddEvent.showMaximized()
    def displayAddVenue(self): 
        self.ui.mdiArea.addSubWindow(self.ui.AddVenue) 
        self.ui.AddVenue.showMaximized()
    def displayAddClient(self): 
        self.ui.mdiArea.addSubWindow(self.ui.AddClient) 
        self.ui.AddClient.showMaximized()
    def displayAllEvents(self): 
        self.ui.mdiArea.addSubWindow(self.ui.ViewAllEvents) 
        self.ui.ViewAllEvents.showMaximized()
    def displayAllClients(self): 
        self.ui.mdiArea.addSubWindow(self.ui.ViewAllClients) 
        self.ui.ViewAllClients.showMaximized()
    def displayAllVenues(self): 
        self.ui.mdiArea.addSubWindow(self.ui.ViewAllVenues) 
        self.ui.ViewAllVenues.showMaximized()



if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv) 
    myapp = MyForm() 
    myapp.show() 
    sys.exit(app.exec_())