# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addQuestion.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\'Images/logo01(Faded).jpg\');\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #ADD8E6;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnteredQuestion = QtWidgets.QTextEdit(self.centralwidget)
        self.EnteredQuestion.setGeometry(QtCore.QRect(10, 10, 621, 64))
        self.EnteredQuestion.setObjectName("EnteredQuestion")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 251, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QuestionImage = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.QuestionImage.setObjectName("QuestionImage")
        self.horizontalLayout.addWidget(self.QuestionImage)
        self.qImageBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.qImageBtn.setObjectName("qImageBtn")
        self.horizontalLayout.addWidget(self.qImageBtn)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 140, 481, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionA = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.optionA.setObjectName("optionA")
        self.verticalLayout.addWidget(self.optionA)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.optionAImage = QtWidgets.QLabel(self.gridLayoutWidget)
        self.optionAImage.setObjectName("optionAImage")
        self.horizontalLayout_3.addWidget(self.optionAImage)
        self.aImageBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.aImageBtn.setObjectName("aImageBtn")
        self.horizontalLayout_3.addWidget(self.aImageBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.optionB = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.optionB.setObjectName("optionB")
        self.verticalLayout_2.addWidget(self.optionB)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.optionAImage_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.optionAImage_2.setObjectName("optionAImage_2")
        self.horizontalLayout_4.addWidget(self.optionAImage_2)
        self.bImageBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bImageBtn.setObjectName("bImageBtn")
        self.horizontalLayout_4.addWidget(self.bImageBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.optionD = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.optionD.setObjectName("optionD")
        self.verticalLayout_4.addWidget(self.optionD)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.optionAImage_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.optionAImage_4.setObjectName("optionAImage_4")
        self.horizontalLayout_6.addWidget(self.optionAImage_4)
        self.cImageBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cImageBtn_2.setObjectName("cImageBtn_2")
        self.horizontalLayout_6.addWidget(self.cImageBtn_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.optionC = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.optionC.setObjectName("optionC")
        self.verticalLayout_3.addWidget(self.optionC)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.optionAImage_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.optionAImage_3.setObjectName("optionAImage_3")
        self.horizontalLayout_5.addWidget(self.optionAImage_3)
        self.bImageBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bImageBtn_2.setObjectName("bImageBtn_2")
        self.horizontalLayout_5.addWidget(self.bImageBtn_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(500, 140, 131, 112))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.opA = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.opA.setObjectName("opA")
        self.verticalLayout_5.addWidget(self.opA)
        self.opB = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.opB.setObjectName("opB")
        self.verticalLayout_5.addWidget(self.opB)
        self.opC = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.opC.setObjectName("opC")
        self.verticalLayout_5.addWidget(self.opC)
        self.opD = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.opD.setObjectName("opD")
        self.verticalLayout_5.addWidget(self.opD)
        self.addQuestionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addQuestionBtn.setGeometry(QtCore.QRect(330, 370, 161, 31))
        self.addQuestionBtn.setObjectName("addQuestionBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QuestionImage.setText(_translate("MainWindow", "Question Image"))
        self.qImageBtn.setText(_translate("MainWindow", "Add Image "))
        self.optionAImage.setText(_translate("MainWindow", "Option A Image"))
        self.aImageBtn.setText(_translate("MainWindow", "Add Image "))
        self.optionAImage_2.setText(_translate("MainWindow", "Option B Image"))
        self.bImageBtn.setText(_translate("MainWindow", "Add Image "))
        self.optionAImage_4.setText(_translate("MainWindow", "Option D Image"))
        self.cImageBtn_2.setText(_translate("MainWindow", "Add Image "))
        self.optionAImage_3.setText(_translate("MainWindow", "Option C Image"))
        self.bImageBtn_2.setText(_translate("MainWindow", "Add Image "))
        self.label.setText(_translate("MainWindow", "Correct Option ??"))
        self.opA.setText(_translate("MainWindow", "A"))
        self.opB.setText(_translate("MainWindow", "B"))
        self.opC.setText(_translate("MainWindow", "C"))
        self.opD.setText(_translate("MainWindow", "D"))
        self.addQuestionBtn.setText(_translate("MainWindow", "Add Question "))