from PyQt5.QtWidgets import QDialog, QMessageBox,  QFileDialog
from testOperation import Test
from startTestUI import Ui_startTest_2
from instructionUI import Ui_InstructionWindow
import sqlite3
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class InstructionWindow(QDialog,Ui_InstructionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Instructions")
        self.proceedButton.clicked.connect(self.proceed)

    def proceed(self):
        self.accept()

#setting up test 
class startTest(QDialog,Ui_startTest_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.testSelect.clicked.connect(self.openTestFile)
        self.startTest.clicked.connect(self.start_Test)
        self.db_file = resource_path(self.testFile.text())
        self.noq = self.noQ.text() # number of questions 
        self.pp = self.percentage.text() # percentage 
        self.tl = self.time.text() # time limit 
        
        
    def start_Test(self):
        self.db_file = resource_path(self.testFile.text())
        self.noq = self.noQ.text()
        self.pp = self.percentage.text()
        self.tl = self.time.text()

        if self.db_file == "open file":
            QMessageBox.warning(
                self, "Warning", "No database file selected.")
        else:
            try:
                if self.db_file:
                    instruction_window = InstructionWindow()
                    if instruction_window.exec_() == QDialog.Accepted:
                        self.test = Test(
                            self.db_file, self.noq, self.tl, self.pp)
                        self.test.showMaximized()
                        self.close()
                else:
                    QMessageBox.warning(
                        self, "Warning", "No database file selected.")
            except Exception as e:
                print("Error:", e)
        
    def openTestFile(self):
        try:
            options = QFileDialog.Options()
            # Filter for .db files
            fileName, _ = QFileDialog.getOpenFileName(self, "Select Test File", "", "Database Files (*.db);;All Files (*)", options=options)
            if fileName:
                # Display the selected file name in the label
                self.testFile.setText(os.path.abspath(fileName))
                self.readTestSettingFromDataBase()
                
        except Exception as e:
            print("Error Loading Test File:", e)
               
    def readTestSettingFromDataBase(self):
        try:
            # Get the database file name from the text of testFile label
            db_file = resource_path(self.testFile.text())
            
            # Establish a connection to the SQLite database
            connection = sqlite3.connect(db_file)
            cursor = connection.cursor()
            
            # Execute a query to retrieve the test settings
            cursor.execute("SELECT num_questions, passing_percentage, time_limit FROM testSettings")
    
            # Fetch the results of the query
            test_settings = cursor.fetchone()
             
            if test_settings:
                # Extract individual settings
                num_questions, passing_percentage, time_limit = test_settings
                
                # Display the settings on respective labels
                self.noQ.setText(str(num_questions))
                self.percentage.setText(str(passing_percentage))
                self.time.setText(str(time_limit))
            else:
                # If no settings are found, display a message
                QMessageBox.warning(self, "Warning", "No test settings found in the database.")
                 
            # Close the database connection
            connection.close()
        except Exception as e:
            print("Error reading test settings from database:", e)
                    
'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startTest()
    window.show()
    sys.exit(app.exec_())'''
    