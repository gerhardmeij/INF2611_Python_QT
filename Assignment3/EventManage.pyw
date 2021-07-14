import sys 
import pickle
from PyQt4.QtGui import *
from EventMan import *

class events:
    def __init__(self):
        self.eventName = "None" 
        self.Client = "None"
        self.Venue = "None"
        self.EntranceFee = "0"
        self.EventLimit = "0"
        self.StartTime = "None"
        self.EndTime = "None"
        self.EventDate = "None"

class clients:
    def _int_(self):
        self.FirstName = "None"
        self.LastName = "None"
        self.Phone = "None"
        self.Email = "None"

class venues:
    def _ini_(self):
        self.VenueName = "None" 
        self.Capacity = "0" 
        self.ContactName = "None" 
        self.ContactNumber = "None" 
        self.Email = "None" 
        self.Address = "None" 
        self.City = "None" 
        self.Province = "None" 
        self.PostalCode = "None" 


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
        QtCore.QObject.connect(self.ui.eventSubmitButton, QtCore.SIGNAL('clicked()'),self.eventSubmit)
        QtCore.QObject.connect(self.ui.clientSubmitButton, QtCore.SIGNAL('clicked()'),self.clientSubmit)
        QtCore.QObject.connect(self.ui.venueSubmitButton, QtCore.SIGNAL('clicked()'),self.venueSubmit)

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

        eventFileRead =  open('eventFile.bin','rb')
        fileDataStoredObj = pickle.load(eventFileRead)
        eventFileRead.close()
        row=0 
        for tup in fileDataStoredObj: 
            col=0
            anitem=QTableWidgetItem(tup.eventName) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Client) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Venue) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.EntranceFee) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.EventLimit) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.StartTime) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.EndTime) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.EndTime) 
            self.ui.eventTableWidget.setItem(row,col, anitem) 
            col+=1
            row+=1 

    def displayAllClients(self): 
        self.ui.mdiArea.addSubWindow(self.ui.ViewAllClients) 
        self.ui.ViewAllClients.showMaximized()

        clientFileRead =  open('clientFile.bin','rb')
        fileDataStoredObj = pickle.load(clientFileRead)
        clientFileRead.close()
        row=0 
        for tup in fileDataStoredObj: 
            col=0
            anitem=QTableWidgetItem(tup.FirstName) 
            self.ui.clientTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.LastName) 
            self.ui.clientTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Phone) 
            self.ui.clientTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Email) 
            self.ui.clientTableWidget.setItem(row,col, anitem) 
            col+=1
            row+=1 

    def displayAllVenues(self): 
        self.ui.mdiArea.addSubWindow(self.ui.ViewAllVenues) 
        self.ui.ViewAllVenues.showMaximized()

        venueFileRead =  open('venueFile.bin','rb')
        fileDataStoredObj = pickle.load(venueFileRead)
        venueFileRead.close()
        row=0 
        for tup in fileDataStoredObj: 
            col=0
            anitem=QTableWidgetItem(tup.VenueName) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Capacity) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.ContactName) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.ContactNumber) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Email) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Address) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.City) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.Province) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            anitem=QTableWidgetItem(tup.PostalCode) 
            self.ui.venueTableWidget.setItem(row,col, anitem) 
            col+=1
            row+=1 

    def eventSubmit(self): 
        newEvent = events()
        newEvent.eventName = self.ui.eventName.text()
        newEvent.Client = self.ui.eventClient.text()
        newEvent.Venue = self.ui.eventVenue.text()
        newEvent.EntranceFee = self.ui.eventFee.text()
        newEvent.EventLimit = self.ui.eventLimit.text()
        newEvent.StartTime = self.ui.eventStartTime.text()
        newEvent.EndTime = self.ui.eventEndTime.text()
        newEvent.EventDate = str(self.ui.eventDate.selectedDate().toPyDate()) 
        testCopy = newEvent

        clientFileRead =  open('eventFile.bin','rb')
        fileDataStoredObj = pickle.load(clientFileRead)
        clientFileRead.close()
        
        if not fileDataStoredObj:
            eventData = [newEvent]
            eventFileWrite = open('eventFile.bin', 'wb')
            pickle.dump(eventData, eventFileWrite)
            eventFileWrite.close()
        else:
            fileDataStoredObj.append(newEvent)
            eventFileWrite = open('eventFile.bin', 'wb')
            pickle.dump(fileDataStoredObj, eventFileWrite)
            eventFileWrite.close()
        
    def clientSubmit(self): 
        newClient = clients()
        newClient.FirstName = self.ui.clientFirstName.text()
        newClient.LastName = self.ui.clientLastName.text()
        newClient.Phone = self.ui.clientPhone.text()
        newClient.Email = self.ui.clientEmail.text()
        testCopy = newClient

        clientFileRead =  open('clientFile.bin','rb')
        fileDataStoredObj = pickle.load(clientFileRead)
        clientFileRead.close()
        
        if not fileDataStoredObj:
            clientData = [newClient]
            clientFileWrite = open('clientFile.bin', 'wb')
            pickle.dump(clientData, clientFileWrite)
            clientFileWrite.close()
        else:
            fileDataStoredObj.append(newClient)
            clientFileWrite = open('clientFile.bin', 'wb')
            pickle.dump(fileDataStoredObj, clientFileWrite)
            clientFileWrite.close()
    
    def venueSubmit(self): 
        newVenue = venues()
        newVenue.VenueName = self.ui.venueName.text()
        newVenue.Capacity = self.ui.venueCapacity.text()
        newVenue.ContactName = self.ui.venueContactName.text()
        newVenue.ContactNumber = self.ui.venueContactNumber.text()
        newVenue.Email = self.ui.venueContactEmail.text()
        newVenue.Address = self.ui.venueAddress.text()
        newVenue.City = self.ui.venueCity.text()
        newVenue.Province = self.ui.venueProvince.text()
        newVenue.PostalCode = self.ui.venuePostalCode.text()
        testCopy = newVenue

        venueFileRead =  open('venueFile.bin','rb')
        fileDataStoredObj = pickle.load(venueFileRead)
        venueFileRead.close()
        
        if not fileDataStoredObj:
            venueData = [newVenue]
            venueFileWrite = open('venueFile.bin', 'wb')
            pickle.dump(venueData, venueFileWrite)
            venueFileWrite.close()
        else:
            fileDataStoredObj.append(newVenue)
            venueFileWrite = open('venueFile.bin', 'wb')
            pickle.dump(fileDataStoredObj, venueFileWrite)
            venueFileWrite.close()


if __name__ == "__main__": 
    app = QtGui.QApplication(sys.argv) 
    myapp = MyForm() 
    myapp.show() 
    sys.exit(app.exec_())