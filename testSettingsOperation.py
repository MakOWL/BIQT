from PyQt5.QtWidgets import QDialog, QMessageBox
from testSettingWindowUI import Ui_testSettings
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

class TestSettingsDialog(QDialog,Ui_testSettings):
    def __init__(self, db_name):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.saveButton.clicked.connect(self.saveTestSettings)  # Connect clicked signal to saveTestSettings method
        
        # Populate line edits with existing values, if any
        self.populateLineEdits()

    def populateLineEdits(self):
        try:
            # Fetch existing test settings from the testSettings table
            self.cur.execute("SELECT num_questions, passing_percentage, time_limit FROM testSettings")
            test_settings = self.cur.fetchone()

            if test_settings:
                num_questions, passing_percentage, time_limit = test_settings
                self.noQuestions.setText(str(num_questions))
                self.passingPercentage.setText(str(passing_percentage))
                self.timeLimit.setText(str(time_limit))
        except Exception as e:
            print("Error fetching test settings:", e)

    def saveTestSettings(self):
        try:
            num_questions = self.noQuestions.text()
            passing_percentage = self.passingPercentage.text()
            time_limit = self.timeLimit.text()
            
            # Check if any line edit is empty
            if not num_questions or not passing_percentage or not time_limit:
                QMessageBox.warning(self, "Error", "Please enter values for all fields.")
                return
            
            try:
                num_questions = int(num_questions)
                passing_percentage = int(passing_percentage)
                time_limit = int(time_limit)
                
                # Check if the number of questions selected is valid
                total_questions = self.cur.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
                if num_questions > total_questions:
                    QMessageBox.warning(self, "Error", "There are not enough questions in the database.")
                    return
                
                # Create a new table for test settings
                self.cur.execute('''CREATE TABLE IF NOT EXISTS testSettings (
                                        id INTEGER PRIMARY KEY,
                                        num_questions INTEGER,
                                        passing_percentage INTEGER,
                                        time_limit INTEGER
                                    )''')
                
                # Delete existing settings (overwrite)
                self.cur.execute("DELETE FROM testSettings")
                
                # Insert new settings
                self.cur.execute("INSERT INTO testSettings (num_questions, passing_percentage, time_limit) VALUES (?, ?, ?)", 
                                (num_questions, passing_percentage, time_limit))
                
                self.conn.commit()
                self.conn.close()
                
                self.accept()  # Close the dialog
            except ValueError:
                # Show error message if input cannot be converted to integers
                QMessageBox.warning(self, "Error", "Invalid input. Please enter integers for number of questions, passing percentage, and time limit.")
        except Exception as e:
            QMessageBox.warning("Error:",e)