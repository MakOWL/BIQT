import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,  QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from addQuestionOperation import AddQuestion
from testSettingsOperation import TestSettingsDialog
from addTest import AddTestDialog
from adminWindowUI import Ui_adminWindow
import sqlite3
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class AdminWindow(QMainWindow,Ui_adminWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newQuestion.clicked.connect(self.open_add_question_window)
        #self.newTest.clicked.connect(self.open_add_test_dialog)
        self.openButton.clicked.connect(self.open_database)
        self.refreshButton.clicked.connect(self.refresh_list)
        self.deleteQuestion.clicked.connect(self.delete_question)
        self.searchButton.clicked.connect(self.search)
        self.testSettings.clicked.connect(self.goto_test_settings)
        self.add_test_dialog = None
        self.db_file = resource_path(self.testFile.text())
        self.questionList.cellClicked.connect(self.display_image)
        #self.aboutToQuit.connect(self.check_test_settings)  # Connect to check_test_settings method when window is about to close
        
    def goto_test_settings(self):
        self.db_file = resource_path(self.testFile.text())
        if self.db_file == "open file":
            QMessageBox.warning(self, "Warning", "No database file selected.")  
        else:  
            try:
                if self.db_file:
                    self.settings_window = TestSettingsDialog(self.db_file)
                    self.settings_window.show()
                    self.load_test_settings()  # Load test settings when the dialog is shown
                else:
                    QMessageBox.warning(self, "Warning", "No database file selected.")
            except Exception as e:
                print("Error:", e)
    
    def closeEvent(self, event):
        # Override the closeEvent method to handle the window closing event
        
        if self.db_file == "open file":
            # If no database file is selected, allow the window to close without any checks
            event.accept()
            return

        if not self.percentageLabel.text() or not self.noqLabel.text() or not self.timeLabel.text():
            reply = QMessageBox.warning(self, "Warning", "Test settings are incomplete. Do you want to open test settings?", QMessageBox.Ok | QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                event.ignore()  # Ignore the close event if the user cancels
                return
            elif reply == QMessageBox.Ok:
                self.goto_test_settings()  # Open the test settings window
                event.ignore()  # Ignore the close event
                return

        # Check if the number of questions specified is greater than the total questions in the database
        if self.noqLabel.text():
            try:
                num_questions_label = int(self.noqLabel.text())
                num_questions_database = self.get_total_questions_in_database()
                if num_questions_database is not None and num_questions_label > num_questions_database:
                    QMessageBox.warning(self, "Warning", f"The number of questions specified ({num_questions_label}) is greater than the total questions in the database ({num_questions_database}). Please adjust the test settings.")
                    event.ignore()  # Ignore the close event
                    return
            except ValueError:
                pass  # Ignore if the number of questions label is not a valid integer

        event.accept()  # Accept the close event if all checks pass

    def get_total_questions_in_database(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM questions")
            total_questions = cursor.fetchone()[0]
            conn.close()
            return total_questions
        except Exception as e:
            print("Error getting total questions:", e)
            return None

    
    def open_database(self):
        self.noqLabel.setText('')
        self.percentageLabel('')
        self.timeLabel('')
        try:
            db_file, _ = QFileDialog.getOpenFileName(self, "Open Database File", "", "Database Files (*.db)")
            print("Selected database file:", db_file)  # Debugging
            db_file = resource_path(db_file)
            
            if db_file:
                db_name = os.path.basename(db_file)
                conn = sqlite3.connect(resource_path(db_name))
                self.testFile.setText(db_name)
                cursor = conn.cursor()
                
                # Fetch questions and options
                cursor.execute("SELECT * FROM questions")
                questions = cursor.fetchall()
                cursor.execute("SELECT * FROM options")
                options = cursor.fetchall()
                
                conn.close()
                
                # Clear the table
                self.questionList.clear()
                self.questionList.setRowCount(0)
                self.questionList.setColumnCount(0)
                
                if questions:
                    # Set headers
                    headers = ["Question"] + [f"Option {i}" for i in range(1, 5)]  # Assuming there are four options
                    self.questionList.setColumnCount(len(headers))
                    self.questionList.setHorizontalHeaderLabels(headers)
                    
                    
                    # Populate table
                    self.questionList.setRowCount(len(questions))
                    for i, question in enumerate(questions):
                        question_text = question[1]
                        question_id = question[0]
                        
                        # Find options for this question
                        question_options = [(opt[2]) for opt in options if opt[1] == question_id]
                        
                        # Set question text
                        self.questionList.setItem(i, 0, QTableWidgetItem(question_text))
                        
                        # Set options
                        for j, option in enumerate(question_options, start=1):
                            self.questionList.setItem(i, j, QTableWidgetItem(option))
                
                self.load_test_settings()  # Load test settings when the database is opened
                self.questionList.resizeRowsToContents()
                self.questionList.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.warning("Error:",e)
    
    def load_test_settings(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            # Fetch test settings from the testSettings table
            cursor.execute("SELECT num_questions, passing_percentage, time_limit FROM testSettings")
            test_settings = cursor.fetchone()
            
            conn.close()
            
            if test_settings:
                num_questions, passing_percentage, time_limit = test_settings
                
                # Update labels with the fetched values
                self.noqLabel.setText(str(num_questions))
                self.percentageLabel.setText(str(passing_percentage))
                self.timeLabel.setText(str(time_limit))
                
        except Exception as e:
            print("Error loading test settings:", e)  
                          
    def display_image(self, row, column):
        try:
            print("Clicked Row:", row)
            print("Clicked Column:", column)
            
            # Get the database file path
            self.db_file = self.testFile.text()
            
            # If no database file is selected, show a warning message and return
            if not self.db_file:
                QMessageBox.warning(self, "Warning", "No database file selected.")
                return

            # Connect to the database
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            item = self.questionList.item(row, column)

            if item is not None:
                cell_text = item.text()
                if column == 0:  
                    cursor.execute("SELECT question_image FROM questions WHERE question_text = ?", (cell_text,))
                else:
                    question_text = self.questionList.item(row, 0).text()
                    cursor.execute("SELECT id FROM questions WHERE question_text = ?", (question_text,))
                    question_id = cursor.fetchone()[0]
                    # Assuming the options are ordered by their IDs, we fetch the option based on its position
                    cursor.execute("SELECT option_image FROM options WHERE question_id = ? LIMIT 1 OFFSET ?", (question_id, column - 1))
                image_blob = cursor.fetchone()

                if image_blob is not None and image_blob[0]:
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_blob[0])
                    self.imageLabel.setPixmap(pixmap)
                    print("image here ")
                else:
                    self.imageLabel.clear()  # Clear any previous image
                    self.imageLabel.setText("No image")
                    print("Hey no image here ")
            else:
                self.imageLabel.clear()  
                self.imageLabel.setText("No image")
                print("its this condition ")

            conn.close()

        except Exception as e:
            print("Error displaying image:", e)

        
    def search(self):
        try:
            searchText = self.searchBar.text().strip()
            if searchText == "":
                QMessageBox.warning(self, "Warning", "Search bar is empty!")
                return
            self.db_file = self.testFile.text()
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            # Search for the text in questions and options
            cursor.execute("SELECT q.id, q.question_text, o.option_text FROM questions q LEFT JOIN options o ON q.id = o.question_id WHERE q.question_text LIKE ? OR o.option_text LIKE ?", ('%'+searchText+'%', '%'+searchText+'%'))
            search_results = cursor.fetchall()
            
            conn.close()
            
            # Clear the table
            self.questionList.clear()
            self.questionList.setRowCount(0)
            self.questionList.setColumnCount(0)
            
            if search_results:
                # Set headers
                headers = ["Question"] + [f"Option {i}" for i in range(1, 5)]  # Assuming there are four options
                self.questionList.setColumnCount(len(headers))
                self.questionList.setHorizontalHeaderLabels(headers)
                
                # Group results by question ID
                grouped_results = {}
                for result in search_results:
                    question_id = result[0]
                    question_text = result[1]
                    option_text = result[2]
                    
                    if question_id not in grouped_results:
                        grouped_results[question_id] = {"question_text": question_text, "options": []}
                    
                    if option_text:
                        grouped_results[question_id]["options"].append(option_text)
                        
                # Populate table
                self.questionList.setRowCount(len(grouped_results))
                for i, (question_id, data) in enumerate(grouped_results.items()):
                    question_text = data["question_text"]
                    options = data["options"]
                    
                    # Set question text
                    self.questionList.setItem(i, 0, QTableWidgetItem(question_text))
                    
                    # Set options in the same row, starting from the second column
                    for j, option in enumerate(options, start=1):
                        self.questionList.setItem(i, j, QTableWidgetItem(option))
                        
        except Exception as e:
            print("Error Searching:", e)
                  
    def open_add_test_dialog(self):
        try:
            self.add_test_dialog = AddTestDialog()
            self.add_test_dialog.exec_()
        except Exception as e:
            print("Error:", e)
        
    def open_add_question_window(self):
        self.db_file = resource_path(self.testFile.text())
        if(self.db_file == "open file"):
          QMessageBox.warning(self, "Warning", "No database file selected.")  
        else:  
            try:
                if self.db_file:
                    self.add_question_window = AddQuestion(self.db_file)
                    self.add_question_window.show()
                else:
                    QMessageBox.warning(self, "Warning", "No database file selected.")
            except Exception as e:
                print("Error:", e)
               
    def load_database(self):
        try:
           # db_name = os.path.basename(self.db_file)
            conn = sqlite3.connect(self.db_file)
            self.testFile.setText(self.db_file)
            cursor = conn.cursor()
            
            # Fetch questions and options
            cursor.execute("SELECT * FROM questions")
            questions = cursor.fetchall()
            cursor.execute("SELECT * FROM options")
            options = cursor.fetchall()
            
            conn.close()
            
            # Clear the table
            self.questionList.clear()
            self.questionList.setRowCount(0)
            self.questionList.setColumnCount(0)
            
            if questions:
                # Set headers
                headers = ["Question"] + [f"Option {i}" for i in range(1, 5)]  # Assuming there are four options
                self.questionList.setColumnCount(len(headers))
                self.questionList.setHorizontalHeaderLabels(headers)
                
                # Populate table
                self.questionList.setRowCount(len(questions))
                for i, question in enumerate(questions):
                    question_text = question[1]
                    question_id = question[0]
                    
                    # Find options for this question
                    question_options = [(opt[2]) for opt in options if opt[1] == question_id]
                    
                    # Set question text
                    self.questionList.setItem(i, 0, QTableWidgetItem(question_text))
                    
                    # Set options
                    for j, option in enumerate(question_options, start=1):
                        self.questionList.setItem(i, j, QTableWidgetItem(option))
                    
        except Exception as e:
            print("Error:", e)  # Debugging
                       
    def open_database(self):
        try:
            db_file, _ = QFileDialog.getOpenFileName(self, "Open Database File", "", "Database Files (*.db)")
            print("Selected database file:", db_file)  # Debugging
            db_file = resource_path(db_file)
            
            if db_file:
                db_name = os.path.abspath(db_file)
                conn = sqlite3.connect(db_name)
                self.testFile.setText(db_name)
                cursor = conn.cursor()
                
                # Fetch questions and options
                cursor.execute("SELECT * FROM questions")
                questions = cursor.fetchall()
                cursor.execute("SELECT * FROM options")
                options = cursor.fetchall()
                
                conn.close()
                
                # Clear the table
                self.questionList.clear()
                self.questionList.setRowCount(0)
                self.questionList.setColumnCount(0)
                
                if questions:
                    # Set headers
                    headers = ["Question"] + [f"Option {i}" for i in range(1, 5)]  # Assuming there are four options
                    self.questionList.setColumnCount(len(headers))
                    self.questionList.setHorizontalHeaderLabels(headers)
                    
                    # Populate table
                    self.questionList.setRowCount(len(questions))
                    for i, question in enumerate(questions):
                        question_text = question[1]
                        question_id = question[0]
                        
                        # Find options for this question
                        question_options = [(opt[2]) for opt in options if opt[1] == question_id]
                        
                        # Set question text
                        self.questionList.setItem(i, 0, QTableWidgetItem(question_text))
                        
                        # Set options
                        for j, option in enumerate(question_options, start=1):
                            self.questionList.setItem(i, j, QTableWidgetItem(option))
                        
        except Exception as e:
            print("Error:", e)  # Debugging
    
    def refresh_list(self):
      try:
        self.db_file = resource_path(self.testFile.text())
        if self.db_file:
            self.load_database()
        else:
            QMessageBox.warning(self, "Warning", "No database file selected.")
      except Exception as e :
         print("Error:", e) 
    
    def delete_question(self):
        self.db_file = resource_path(self.testFile.text())
        try:
            selected_row = self.questionList.currentRow()
            if selected_row != -1:  # Check if any row is selected
                question_text = self.questionList.item(selected_row, 0).text()  # Assuming the question is in the first column

                # Prompt the user with a confirmation message
                reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this question?', 
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    # Connect to the database
                    conn = sqlite3.connect(self.db_file)
                    cursor = conn.cursor()

                    # Fetch the question ID using its text
                    cursor.execute("SELECT id FROM questions WHERE question_text = ?", (question_text,))
                    question_id = cursor.fetchone()[0]

                    # Delete the question from the questions table
                    cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))

                    # Delete the associated options from the options table
                    cursor.execute("DELETE FROM options WHERE question_id = ?", (question_id,))

                    # Commit changes and close the connection
                    conn.commit()
                    conn.close()

                    # Remove the row from the table
                    self.questionList.removeRow(selected_row)

                    QMessageBox.information(self, "Information", "Question deleted successfully.")
            else:
                QMessageBox.warning(self, "Warning", "Please select a question to delete.")
        except Exception as e:
            print("Error:", e)  # Debugging
                    
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        admin_window = AdminWindow()
        admin_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)