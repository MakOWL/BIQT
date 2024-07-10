from PyQt5.QtWidgets import QDialog
from resultScreenUI import Ui_Result


class resultWindow(QDialog,Ui_Result):
    def __init__(self,rea,total,correct,incorrect,missed,percentage,passOrFail):
        super().__init__()
        self.setupUi(self)
        self.reason.setText(str(rea))
        self.total.setText(str(total))
        self.answered.setText(str(correct + incorrect))
        self.unanswered.setText(str(missed))
        self.correct.setText(str(correct))
        self.incorrect.setText(str(incorrect))
        self.percentage.setText(str(percentage))
        self.result_status.setText(str(passOrFail))