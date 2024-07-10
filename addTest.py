from PyQt5.QtWidgets import  QDialog, QMessageBox
from addTestDialogUI import Ui_AddTestDialog
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

class AddTestDialog(QDialog,Ui_AddTestDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.createButton.clicked.connect(self.create_test_database)

    def create_test_database(self):
        test_name = self.lineEdit.text().strip()
        if not test_name:
            QMessageBox.warning(self, "Warning", "Please enter a valid test name.")
            return

        # Create a new database file in the data folder
        try:
            data_folder = "data"
            if not os.path.exists(data_folder):
                os.makedirs(data_folder)
            db_name = os.path.join(data_folder, f"{test_name}.db")

            conn = sqlite3.connect(resource_path(db_name))
            cursor = conn.cursor()
            cursor = conn.cursor()

            # Create tables
            cursor.execute('''CREATE TABLE IF NOT EXISTS options (
                                id INTEGER PRIMARY KEY,
                                question_id INTEGER,
                                option_text TEXT,
                                option_image BLOB,
                                is_correct BOOLEAN,
                                FOREIGN KEY (question_id) REFERENCES questions(id)
                            )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                                id INTEGER PRIMARY KEY,
                                question_text TEXT,
                                question_image BLOB,
                                correct_option_index INTEGER
                            )''')

            # Create testSettings table if it doesn't exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS testSettings (
                        id INTEGER PRIMARY KEY,
                        num_questions INTEGER DEFAULT 0,
                        passing_percentage INTEGER DEFAULT 0,
                        time_limit INTEGER DEFAULT 0
                    )''')

            conn.commit()
            conn.close()
            QMessageBox.information(self, "Information", f"Test '{test_name}' created successfully.")
            self.close()
        except Exception as e:
            QMessageBox.warning("Error:",e)
            
