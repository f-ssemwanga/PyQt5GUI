#import required modules
from  PyQt5 import QtCore, QtGui, QtWidgets, uic
#from PyQt5.QtCore import Qt

#widget class
class Ui(QtWidgets.QMainWindow):
    #this changes based on the class used in the XML file
    '''Constructor'''
    def __init__(self):
        super(Ui, self).__init__() #call to the inherited class' constructor method
        uic.loadUi('logonScreen.ui',self) #loads the uic file 
        
        #Button event listeners / connection to buttons on the form
        self.btnLogin.clicked.connect(self.loginButtonMethod)
        self.btnClear.clicked.connect(self.clearButtonMethod)
        
        self.show()
   
    #Event handler methods are added here
    def loginButtonMethod(self):
        username = self.userNameInput.text().lower()
        password = self.passwordInput.text()     
        print(f'username: {username}| password: {password}')  # only for testing purposes
        
        '''Perform some validation - presence check! and display appropriate message box'''
        if username =="" or password =="":
            messageBox('Blank Fields detected!','You must enter a username and password!', 'warning')
            
        
    def clearButtonMethod(self):
        print('Clear Button was clicked')




#create a messageBox function to display warnings and confirmations
def messageBox(title, content,iconType="info"):
    #creates a message box object
    msgBox =QtWidgets.QMessageBox()
    #set the message box icon based on icon type passed
    if iconType =="info":
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
    elif iconType =="question":
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
    elif iconType =="warning":
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    else:
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        #Set title and content password into the method
    msgBox.setText(content)
    msgBox.setWindowTitle(title)        
    #show the message box
    msgBox.exec()
   
   
    
def mainApplication():
    app = QtWidgets.QApplication ([]) 
    window = Ui() # creates window object from the constructor
    app.exec_()
mainApplication()