# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Result(object):
    def setupUi(self, Result):
        Result.setObjectName("Result")
        Result.resize(400, 300)
        Result.setStyleSheet("QDailog{\n"
"background-image: url(\'Images/logo01(Faded).jpg\');\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #ADD8E6;\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(Result)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 321, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.result_status = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.result_status.setFont(font)
        self.result_status.setObjectName("result_status")
        self.gridLayout.addWidget(self.result_status, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.total = QtWidgets.QLabel(self.gridLayoutWidget)
        self.total.setText("")
        self.total.setObjectName("total")
        self.horizontalLayout_7.addWidget(self.total)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.answered = QtWidgets.QLabel(self.gridLayoutWidget)
        self.answered.setText("")
        self.answered.setObjectName("answered")
        self.horizontalLayout.addWidget(self.answered)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.unanswered = QtWidgets.QLabel(self.gridLayoutWidget)
        self.unanswered.setText("")
        self.unanswered.setObjectName("unanswered")
        self.horizontalLayout_3.addWidget(self.unanswered)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.correct = QtWidgets.QLabel(self.gridLayoutWidget)
        self.correct.setText("")
        self.correct.setObjectName("correct")
        self.horizontalLayout_4.addWidget(self.correct)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.incorrect = QtWidgets.QLabel(self.gridLayoutWidget)
        self.incorrect.setText("")
        self.incorrect.setObjectName("incorrect")
        self.horizontalLayout_5.addWidget(self.incorrect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.percentage = QtWidgets.QLabel(self.gridLayoutWidget)
        self.percentage.setText("")
        self.percentage.setObjectName("percentage")
        self.horizontalLayout_2.addWidget(self.percentage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        self.reason = QtWidgets.QLabel(Result)
        self.reason.setGeometry(QtCore.QRect(40, 10, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.reason.setFont(font)
        self.reason.setStyleSheet("QDailog{\n"
"background-image: url(\'logo01(Faded).jpg\');\n"
"}")
        self.reason.setObjectName("reason")

        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslateUi(self, Result):
        _translate = QtCore.QCoreApplication.translate
        Result.setWindowTitle(_translate("Result", "Result"))
        self.result_status.setText(_translate("Result", "Pass or Fail"))
        self.label_8.setText(_translate("Result", "Result:"))
        self.label_9.setText(_translate("Result", "Total:"))
        self.label_2.setText(_translate("Result", "Answerd: "))
        self.label_4.setText(_translate("Result", "Unaswered:"))
        self.label_5.setText(_translate("Result", "Correct: "))
        self.label_6.setText(_translate("Result", "Incorrect: "))
        self.label_7.setText(_translate("Result", "Percentage:"))
        self.reason.setText(_translate("Result", "Time Up"))
