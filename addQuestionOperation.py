import sqlite3
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QMessageBox
from PyQt5.QtGui import QPixmap
from addQuestion import Ui_MainWindow
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
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

class AddQuestion(QMainWindow,Ui_MainWindow):
    def __init__(self,db_name):
        super().__init__()
        self.setupUi(self)
        # Set the fixed size policy for the window
        self.setFixedSize(self.size())
        # Initialize database connection
        self.conn = sqlite3.connect(resource_path(db_name))
        self.cur = self.conn.cursor()
        
        # Connect the button clicks to functions
        self.qImageBtn.clicked.connect(self.select_image)
        self.aImageBtn.clicked.connect(self.select_option_a_image)
        self.bImageBtn.clicked.connect(self.select_option_b_image)
        self.bImageBtn_2.clicked.connect(self.select_option_c_image)
        self.cImageBtn_2.clicked.connect(self.select_option_d_image)
        self.addQuestionBtn.clicked.connect(self.add_question_to_database)
          
        
    def select_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Select Image", "","Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.QuestionImage.setPixmap(pixmap)
            self.QuestionImage.setScaledContents(True) # Fit the image to the label
            
    def select_option_a_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Select Image for Option A", "","Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.optionAImage.setPixmap(pixmap)
            self.optionAImage.setScaledContents(True)
    
    def select_option_b_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Select Image for Option B", "","Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.optionAImage_2.setPixmap(pixmap)
            self.optionAImage_2.setScaledContents(True)
    
    def select_option_c_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Select Image for Option C", "","Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.optionAImage_3.setPixmap(pixmap)
            self.optionAImage_3.setScaledContents(True)
    
    def select_option_d_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Select Image for Option D", "","Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.optionAImage_4.setPixmap(pixmap)
            self.optionAImage_4.setScaledContents(True)
            
    
    def pixmap_to_blob(self,label):
        pixmap = label.pixmap()
        if pixmap is None:  # Check if no pixmap is set
         return None
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG")
        return byte_array
          
    def add_question_to_database(self):
        try:
            # Check if question statement is provided
            question_text = self.EnteredQuestion.toPlainText().strip()
            if not question_text:
                QMessageBox.warning(self, "Warning", "Please enter a question statement.")
                return

            # Check if correct option is selected
            if not (self.opA.isChecked() or self.opB.isChecked() or self.opC.isChecked() or self.opD.isChecked()):
                QMessageBox.warning(self, "Warning", "Please select a correct option.")
                return

            # Check if each option has either text or image provided
            if not (
                (self.optionA.toPlainText() or self.pixmap_to_blob(self.optionAImage)) and
                (self.optionB.toPlainText() or self.pixmap_to_blob(self.optionAImage_2)) and
                (self.optionC.toPlainText() or self.pixmap_to_blob(self.optionAImage_3)) and
                (self.optionD.toPlainText() or self.pixmap_to_blob(self.optionAImage_4))
            ):
                QMessageBox.warning(self, "Warning", "Please provide either text or image for all options.")
                return

            # Determine correct option index
            if self.opA.isChecked():
                correct_option_index = 1
            elif self.opB.isChecked():
                correct_option_index = 2
            elif self.opC.isChecked():
                correct_option_index = 3
            elif self.opD.isChecked():
                correct_option_index = 4
      
            # Insert question data into the questions table
            question_image_blob = self.pixmap_to_blob(self.QuestionImage)
            self.cur.execute("""INSERT INTO questions (question_text, question_image, correct_option_index) VALUES (?, ?, ?)""",
                            (question_text, question_image_blob, correct_option_index))
            question_id = self.cur.lastrowid
            
            # Insert option data into the options table
            options = [
                (question_id, self.optionA.toPlainText(), self.pixmap_to_blob(self.optionAImage), self.opA.isChecked()),
                (question_id, self.optionB.toPlainText(), self.pixmap_to_blob(self.optionAImage_2), self.opB.isChecked()),
                (question_id, self.optionC.toPlainText(), self.pixmap_to_blob(self.optionAImage_3), self.opC.isChecked()),
                (question_id, self.optionD.toPlainText(), self.pixmap_to_blob(self.optionAImage_4), self.opD.isChecked())
            ]
            self.cur.executemany("""INSERT INTO options (question_id, option_text, option_image, is_correct) VALUES (?, ?, ?, ?)""",
                                options)

            # Commit changes and close database connection
            self.conn.commit()
            print("Data successfully added to the database.")
            self.conn.close()
            self.close()  # Close the add question window after adding the question
        except Exception as e:
            print("Error inserting data:", e)
            self.conn.close()

'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = AddQuestion()
    ui.show()
    sys.exit(app.exec_())'''



