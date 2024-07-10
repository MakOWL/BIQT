# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testWindow(object):
    def setupUi(self, testWindow):
        testWindow.setObjectName("testWindow")
        testWindow.resize(859, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(testWindow.sizePolicy().hasHeightForWidth())
        testWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        testWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        testWindow.setWindowIcon(icon)
        testWindow.setWindowOpacity(1.0)
        testWindow.setAutoFillBackground(False)
        testWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\'images/logo01(Faded Croped).jpg\');\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(testWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.attempted = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.attempted.setFont(font)
        self.attempted.setObjectName("attempted")
        self.horizontalLayout_4.addWidget(self.attempted)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.option0Image = QtWidgets.QLabel(self.centralwidget)
        self.option0Image.setMinimumSize(QtCore.QSize(200, 200))
        self.option0Image.setMaximumSize(QtCore.QSize(300, 300))
        self.option0Image.setAutoFillBackground(False)
        self.option0Image.setStyleSheet("background-color: transparent; \n"
"color: transparent;")
        self.option0Image.setText("")
        self.option0Image.setObjectName("option0Image")
        self.gridLayout_2.addWidget(self.option0Image, 1, 0, 1, 1)
        self.option0 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option0.setFont(font)
        self.option0.setStyleSheet("border: 1px solid #000000;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:white;\n"
"")
        self.option0.setObjectName("option0")
        self.gridLayout_2.addWidget(self.option0, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.option1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option1.setFont(font)
        self.option1.setStyleSheet("border: 1px solid #000000;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:white;\n"
"")
        self.option1.setObjectName("option1")
        self.gridLayout_3.addWidget(self.option1, 0, 0, 1, 1)
        self.option1Image = QtWidgets.QLabel(self.centralwidget)
        self.option1Image.setMinimumSize(QtCore.QSize(200, 200))
        self.option1Image.setMaximumSize(QtCore.QSize(300, 300))
        self.option1Image.setAutoFillBackground(False)
        self.option1Image.setStyleSheet("background-color: transparent; color: transparent;")
        self.option1Image.setText("")
        self.option1Image.setObjectName("option1Image")
        self.gridLayout_3.addWidget(self.option1Image, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.option2Image = QtWidgets.QLabel(self.centralwidget)
        self.option2Image.setMinimumSize(QtCore.QSize(200, 200))
        self.option2Image.setMaximumSize(QtCore.QSize(300, 300))
        self.option2Image.setAutoFillBackground(False)
        self.option2Image.setStyleSheet("background-color: transparent; color: transparent;")
        self.option2Image.setText("")
        self.option2Image.setObjectName("option2Image")
        self.gridLayout_4.addWidget(self.option2Image, 1, 0, 1, 1)
        self.option2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option2.setFont(font)
        self.option2.setStyleSheet("border: 1px solid #000000;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:white;\n"
"")
        self.option2.setObjectName("option2")
        self.gridLayout_4.addWidget(self.option2, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.option3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option3.setFont(font)
        self.option3.setStyleSheet("border: 1px solid #000000;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:white;\n"
"")
        self.option3.setObjectName("option3")
        self.gridLayout_5.addWidget(self.option3, 0, 0, 1, 1)
        self.option3Image = QtWidgets.QLabel(self.centralwidget)
        self.option3Image.setMinimumSize(QtCore.QSize(200, 200))
        self.option3Image.setMaximumSize(QtCore.QSize(300, 300))
        self.option3Image.setAutoFillBackground(False)
        self.option3Image.setStyleSheet("background-color: transparent; \n"
"color: transparent;")
        self.option3Image.setText("")
        self.option3Image.setScaledContents(False)
        self.option3Image.setObjectName("option3Image")
        self.gridLayout_5.addWidget(self.option3Image, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_5)
        self.gridLayout_6.addLayout(self.horizontalLayout_5, 1, 0, 1, 5)
        self.finishButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finishButton.setFont(font)
        self.finishButton.setAutoFillBackground(False)
        self.finishButton.setStyleSheet("background-color: #ADD8E6;")
        self.finishButton.setObjectName("finishButton")
        self.gridLayout_6.addWidget(self.finishButton, 3, 4, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.remainingQuestions = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remainingQuestions.setFont(font)
        self.remainingQuestions.setObjectName("remainingQuestions")
        self.horizontalLayout_3.addWidget(self.remainingQuestions)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 3, 2, 1, 1)
        self.Question = QtWidgets.QLabel(self.centralwidget)
        self.Question.setMinimumSize(QtCore.QSize(100, 100))
        self.Question.setMaximumSize(QtCore.QSize(10000, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Question.setFont(font)
        self.Question.setStyleSheet("border: 1px solid #000000;\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"background-color:white;\n"
"")
        self.Question.setScaledContents(True)
        self.Question.setObjectName("Question")
        self.gridLayout_6.addWidget(self.Question, 0, 1, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.previousButton.setFont(font)
        self.previousButton.setAutoFillBackground(False)
        self.previousButton.setStyleSheet("background-color: #ADD8E6;")
        self.previousButton.setObjectName("previousButton")
        self.gridLayout.addWidget(self.previousButton, 0, 0, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextButton.setFont(font)
        self.nextButton.setAutoFillBackground(False)
        self.nextButton.setStyleSheet("background-color: #ADD8E6;")
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 0, 2, 1, 1)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setAutoFillBackground(False)
        self.submitButton.setStyleSheet("background-color: #ADD8E6;")
        self.submitButton.setObjectName("submitButton")
        self.gridLayout.addWidget(self.submitButton, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 2, 1, 1, 3)
        self.QuestionImage = QtWidgets.QLabel(self.centralwidget)
        self.QuestionImage.setMinimumSize(QtCore.QSize(200, 200))
        self.QuestionImage.setMaximumSize(QtCore.QSize(300, 400))
        self.QuestionImage.setText("")
        self.QuestionImage.setScaledContents(True)
        self.QuestionImage.setObjectName("QuestionImage")
        self.gridLayout_6.addWidget(self.QuestionImage, 0, 3, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.remainingTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remainingTime.setFont(font)
        self.remainingTime.setObjectName("remainingTime")
        self.horizontalLayout_2.addWidget(self.remainingTime)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 3, 3, 1, 1)
        testWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(testWindow)
        self.statusbar.setObjectName("statusbar")
        testWindow.setStatusBar(self.statusbar)

        self.retranslateUi(testWindow)
        QtCore.QMetaObject.connectSlotsByName(testWindow)

    def retranslateUi(self, testWindow):
        _translate = QtCore.QCoreApplication.translate
        testWindow.setWindowTitle(_translate("testWindow", "Test"))
        self.label_3.setText(_translate("testWindow", "Atempted: "))
        self.attempted.setText(_translate("testWindow", "0"))
        self.option0.setText(_translate("testWindow", "Option A"))
        self.option1.setText(_translate("testWindow", "Option B"))
        self.option2.setText(_translate("testWindow", "Option C"))
        self.option3.setText(_translate("testWindow", "Option D"))
        self.finishButton.setText(_translate("testWindow", "Finish Test "))
        self.label_2.setText(_translate("testWindow", "Question: "))
        self.remainingQuestions.setText(_translate("testWindow", "0 out of total"))
        self.Question.setText(_translate("testWindow", "Question"))
        self.previousButton.setText(_translate("testWindow", "Previous"))
        self.nextButton.setText(_translate("testWindow", "Next"))
        self.submitButton.setText(_translate("testWindow", "Submit"))
        self.label.setText(_translate("testWindow", "Time: "))
        self.remainingTime.setText(_translate("testWindow", "Remaining time "))
