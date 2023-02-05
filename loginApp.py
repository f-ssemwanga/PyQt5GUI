#import required modules
from  PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3

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
        enteredUsername = self.userNameInput.text().lower()
        enteredPassword = self.passwordInput.text()     
        print(f'username: {enteredUsername}| password: {enteredPassword}')  # only for testing purposes
        
        '''Perform some validation - presence check! and display appropriate message box'''
        if enteredUsername =="" or enteredPassword =="":
            messageBox('Blank Fields detected!','You must enter a username and password!', 'warning')
        else:
            cred =selectStatementHelper('password','users','username',(enteredUsername,))
            self.clearButtonMethod()
            try:
                if cred[0][0] ==enteredPassword:
                    #inform user that they logged in successfuly
                    messageBox('Login success', 'You have loggin in successfully!')
            except IndexError:
                messageBox('Login failed!', 'Incorrect credentials entered. Please try agan','warning')
        
    def clearButtonMethod(self):
        #clear button functionality
        self.userNameInput.setText('')
        self.passwordInput.setText('')


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
#connecting to the database
def connection():
    #this method establishes a connection to the database
    con =sqlite3.connect('userAndFilms.db')
    cur = con.cursor()
    return con, cur   
def executeStatementHelper(query, args=None):
    #connects and executes a given query on the database
    con,cur = connection()
    if not args:
        cur.execute(query)
    else:
        cur.execute(query, args)
    #fetch data from the database and return it into the variable "selectedData"
    selectedData = cur.fetchall()
    #commit changes if there are any, close connection and return data
    con.commit()
    con.close()
    return selectedData
def selectStatementHelper(fields,table,criteria =None, args=None):
    #constructs a select statement based on entered arguments
    if not criteria:
        query = f'SELECT {fields} FROM {table}'
    else:
        query =f'''SELECT {fields} FROM {table}
        WHERE {criteria}=?'''
    #return results of execution of the query using the execute statement helper
    return(query,args)

    
def mainApplication():
    app = QtWidgets.QApplication ([]) 
    window = Ui() # creates window object from the constructor
    app.exec_()
mainApplication()