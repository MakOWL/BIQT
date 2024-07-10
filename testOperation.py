from PyQt5.QtWidgets import  QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from result import resultWindow
from testUI import Ui_testWindow
import sqlite3

class Test(QMainWindow,Ui_testWindow):
    def __init__(self, db_file, noq, tl, pp):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()        
        self.time_limit_minutes = int(tl)
        self.remaining_time_seconds = self.time_limit_minutes * 60
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.numberOfQuestions = int(noq)
        self.passingPercentage = int(pp)
        self.load_questions(int(noq))
        self.obtainPercentage = 0
        self.correct_answers = 0
        self.incorrect_answers = 0 
        self.unanswered = 0
        self.answered = 0 
        self.current_question_index = 0
        self.resultStatus = '\0'
        self.load_question(self.current_question_index)
        self.nextButton.clicked.connect(self.next_question)
        self.previousButton.clicked.connect(self.previous_question)
        self.remainingQuestions.setText(f"{1} by {self.numberOfQuestions}")
        self.option0.clicked.connect(lambda: self.store_selected_option_index(0))
        self.option1.clicked.connect(lambda: self.store_selected_option_index(1))
        self.option2.clicked.connect(lambda: self.store_selected_option_index(2))
        self.option3.clicked.connect(lambda: self.store_selected_option_index(3))
        self.setOptionsToFalse()
        self.answered_questions = set()  
        self.submitButton.setEnabled(True)  # Ensure the submit button starts enabled
        self.submitButton.clicked.connect(self.submit_confirmation)
        self.finishButton.clicked.connect(self.finish_confirmation)
        self.test_finished = False  # Flag to track if the test is finished
        
    
        

    def endTest(self):
        if not self.test_finished:  # Check if the test is not already finished
            reply = QMessageBox.question(self, 'Finish Confirmation', 'Are you sure you want to finish the test?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                rea = "Finished"
                self.makeResult(rea)
                self.timer.stop()  # Stop the timer when the test finishes
                self.close()  # Close the test window
                self.test_finished = True  # Update the flag to indicate the test is finished

    def update_timer(self):
        # Calculate remaining minutes and seconds
        minutes = self.remaining_time_seconds // 60
        seconds = self.remaining_time_seconds % 60
        
        # Convert to formatted string
        time_text = "{:02d}:{:02d}".format(minutes, seconds)

        # Update the label text with the remaining time
        self.remainingTime.setText(time_text)
        
        # Decrease remaining seconds
        self.remaining_time_seconds -= 1
        
        # Stop the timer when time reaches zero
        if self.remaining_time_seconds < 0 and not self.test_finished:  # Check if the test is not already finished
            rea = "Time UP !!"
            self.makeResult(rea)
            self.timer.stop()  # Stop the timer when the test finishes
            self.close()  # Close the test window
            self.test_finished = True
            
    def finish_confirmation(self):
        if not self.test_finished:  # Check if the test is not already finished
            reply = QMessageBox.question(self, 'Finish Confirmation', 'Are you sure you want to finish the test?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                rea = "Finished"
                self.makeResult(rea)
                self.timer.stop()  # Stop the timer when the test finishes
                self.close()  # Close the test window
                self.test_finished = True  # Update the flag to indicate the test is finished

        
    def setOptionsToFalse(self):
        try:
            self.option0.setChecked(False)
            self.option1.setChecked(False)
            self.option2.setChecked(False)
            self.option3.setChecked(False)
        except Exception as e:
            print("Error settingup option to false",e)
        
    def endTest(self):
        rea = "Finished"
        self.makeResult(rea)        
    
    def makeResult(self,rea):  
            self.obtainPercentage = (self.correct_answers/self.numberOfQuestions) * 100
            if self.obtainPercentage >= self.passingPercentage:
                self.resultStatus = "Pass"
                self.showResultScreen(self.numberOfQuestions,rea, self.correct_answers, self.incorrect_answers, self.unanswered, self.obtainPercentage, self.resultStatus)
            else:
                self.resultStatus = "Fail"
                self.showResultScreen(self.numberOfQuestions,rea, self.correct_answers, self.incorrect_answers, self.unanswered, self.obtainPercentage, self.resultStatus)

            
        
    #total,correct,incorrect,missed,percentage,passOrFail       
    def showResultScreen(self,rea,total,correct,incorrect,missed,percentage,passOrFail):  
            try:
                self.resultWindow = resultWindow(total,rea,correct,incorrect,missed,percentage,passOrFail)
                self.resultWindow.show()
            except Exception as e:
                print("Error:", e)
        
    def store_selected_option_index(self, index):
        self.selected_option_index = index
    
    def submit_confirmation(self):
        # Check if the user wants to submit
        reply = QMessageBox.question(self, 'Submit Confirmation', 'Are you sure you want to submit the answer?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.submit_answer()

    def submit_answer(self):
        try:
            self.setOptionsToFalse()
            if self.answered >= self.numberOfQuestions:
                QMessageBox.warning(self, "All Questions Answered", "You have already answered all the questions.")
            elif hasattr(self, 'selected_option_index'):
                self.answered += 1 
                self.attempted.setText(str(self.answered))
                self.submitButton.setEnabled(False)
                self.answered_questions.add(self.current_question_index)  # Update answered questions
                
                selected_option_index = self.selected_option_index
                correct_option_index = self.questions[self.current_question_index]['correct_option_index']
                if selected_option_index == correct_option_index - 1:
                    self.correct_answers += 1 
                    print("Correct answer!")
                else:
                    self.incorrect_answers += 1 
                    print("Incorrect answer!")
                
                self.unanswered = self.numberOfQuestions - (self.correct_answers + self.incorrect_answers)   
                self.next_question()
            else:
                QMessageBox.warning(self, "No Option Selected", "Please select an option before submitting.")
        except Exception as e:
            print("Error Making Result:", e)

        
    def load_questions(self, noq):
        self.questions = []
        self.cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT ?", (noq,))
        rows = self.cursor.fetchall()
        for row in rows:
            self.questions.append({
                'id': row[0],
                'text': row[1],
                'image': row[2],
                'correct_option_index': row[3]
            })
    
    def load_question(self, index):
        try:
            question_data = self.questions[index]
            question_number = index + 1  # Question number starting from 1
            self.Question.setText(f"{question_number}. {question_data['text']}")  # Add question number
            if question_data['image']:
                question_image_pixmap = self.create_pixmap_from_blob(question_data['image'])
                self.QuestionImage.setPixmap(question_image_pixmap) 
                self.QuestionImage.setScaledContents(True)
            else:
                self.QuestionImage.clear()

            self.cursor.execute("SELECT * FROM options WHERE question_id = ?", (question_data['id'],))
            options = self.cursor.fetchall()
            self.setOptionsToFalse()
            option_letters = ['A', 'B', 'C', 'D']  # Option letters
            for i, option in enumerate(options):
                option_text = option[2] 
                option_image_blob = option[3]
                option_image_pixmap = self.create_pixmap_from_blob(option_image_blob)  
                option_widget = getattr(self, f"option{i}") 
                option_image_label = getattr(self, f"option{i}Image")
                
                option_widget.setChecked(False) 
                option_widget.setText(f"{option_letters[i]}. {option_text}")  # Add option letter
                option_image_label.setPixmap(option_image_pixmap)
                option_image_label.setScaledContents(True)

        except Exception as e:
            print("Error:", e)

    def create_pixmap_from_blob(self, blob_data):
        pixmap = QPixmap()
        pixmap.loadFromData(blob_data)
        return pixmap
            
    def next_question(self):
        self.setOptionsToFalse()
        if self.current_question_index == self.numberOfQuestions - 1:
            self.nextButton.setEnabled(False)
            self.nextButton.setStyleSheet("background-color: #E0E0E0; color: #A0A0A0;")  # Example styling for faded look
        else:
            self.nextButton.setEnabled(True)
            self.nextButton.setStyleSheet("")  # Reset to default style
            self.current_question_index += 1
            self.load_question(self.current_question_index)
            self.remainingQuestions.setText(f"{self.current_question_index + 1} by {self.numberOfQuestions}")

        # Disable the submit button for the current question if it has been answered
        if self.current_question_index in self.answered_questions:
            self.submitButton.setEnabled(False)
        else:
            self.submitButton.setEnabled(True)

        # Enable the previous button unless we're on the first question
        if self.current_question_index > 0:
            self.previousButton.setEnabled(True)
            self.previousButton.setStyleSheet("")  # Reset to default style
        else:
            self.previousButton.setEnabled(False)
            self.previousButton.setStyleSheet("background-color: #E0E0E0; color: #A0A0A0;")  # Example styling for faded look

    def previous_question(self):
        self.setOptionsToFalse()
        if self.current_question_index == 0:
            self.previousButton.setEnabled(False)
            self.previousButton.setStyleSheet("background-color: #E0E0E0; color: #A0A0A0;")  # Example styling for faded look
        else:
            self.previousButton.setEnabled(True)
            self.previousButton.setStyleSheet("")  # Reset to default style
            self.current_question_index -= 1
            self.load_question(self.current_question_index)
            self.remainingQuestions.setText(f"{self.current_question_index + 1} by {self.numberOfQuestions}")

        # Disable the submit button for the current question if it has been answered
        if self.current_question_index in self.answered_questions:
            self.submitButton.setEnabled(False)
        else:
            self.submitButton.setEnabled(True)

        # Enable the next button unless we're on the last question
        if self.current_question_index < self.numberOfQuestions - 1:
            self.nextButton.setEnabled(True)
            self.nextButton.setStyleSheet("")  # Reset to default style
        else:
            self.nextButton.setEnabled(False)
            self.nextButton.setStyleSheet("background-color: #E0E0E0; color: #A0A0A0;") 
    
        def update_timer(self):
            # Calculate remaining minutes and seconds
            minutes = self.remaining_time_seconds // 60
            seconds = self.remaining_time_seconds % 60
            
            # Convert to formatted string
            time_text = "{:02d}:{:02d}".format(minutes, seconds)

            # Update the label text with the remaining time
            self.remainingTime.setText(time_text)
            
            # Decrease remaining seconds
            self.remaining_time_seconds -= 1
            
            # Stop the timer and close the window when time reaches zero
            if self.remaining_time_seconds < 0 and not self.test_finished:  # Check if the test is not already finished
                rea = "Time UP !!"
                self.makeResult(rea)
                self.timer.stop()  # Stop the timer when the test finishes
                self.close()  # Close the test window
                self.test_finished = True