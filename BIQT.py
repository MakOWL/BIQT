import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit,QMessageBox
from adminOperation import AdminWindow
from Test import startTest
from BIQT_MainWindow import Ui_MainWindow


class BIQT(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settingsButton.clicked.connect(self.open_admin_window)
        self.startButton.clicked.connect(self.open_test_window)
        
    def open_test_window(self):
        # Prompt the user before opening the test window
        reply = QMessageBox.question(self, 'Confirmation', 'Once the test starts, the current window will close. Do you wish to proceed?', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.test_window = startTest()
            self.close()
            self.test_window.show()
            #self.test_window.showMaximized()  # or any other desired method to show the window
        else:
            pass

    def closeEvent(self, event):
        if hasattr(self, 'admin_window'):
            self.admin_window.close()
        event.accept()
 

    def open_admin_window(self):
        print("Opening admin window")
        pass_key, ok = QInputDialog.getText(self, "Enter Pass Key", "Enter pass key:", QLineEdit.Password)
        if ok and pass_key == "556450":
            print("Correct pass key entered. Opening admin operation window...")
            self.admin_window = AdminWindow()
            self.admin_window.showMaximized()  
            
        else:
           QMessageBox.warning(self, "Incorrect Pass Key", "Incorrect pass key entered. Access denied.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BIQT()
    window.showMaximized()
    sys.exit(app.exec_())
