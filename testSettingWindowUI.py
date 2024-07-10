# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testSettingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testSettings(object):
    def setupUi(self, testSettings):
        testSettings.setObjectName("testSettings")
        testSettings.resize(400, 300)
        testSettings.setStyleSheet("QDailog{\n"
"background-image: url(\'Image/logo01(Faded).jpg\');\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #ADD8E6;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(testSettings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 341, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.noQuestions = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.noQuestions.setObjectName("noQuestions")
        self.horizontalLayout.addWidget(self.noQuestions)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.passingPercentage = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passingPercentage.setObjectName("passingPercentage")
        self.horizontalLayout_2.addWidget(self.passingPercentage)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.timeLimit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.timeLimit.setObjectName("timeLimit")
        self.horizontalLayout_3.addWidget(self.timeLimit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(testSettings)
        QtCore.QMetaObject.connectSlotsByName(testSettings)

    def retranslateUi(self, testSettings):
        _translate = QtCore.QCoreApplication.translate
        testSettings.setWindowTitle(_translate("testSettings", "Test Settings "))
        self.label.setText(_translate("testSettings", "Number of Questions "))
        self.label_2.setText(_translate("testSettings", "Passing Percentage "))
        self.label_3.setText(_translate("testSettings", "Time Limit in Minuts"))
        self.saveButton.setText(_translate("testSettings", "Save"))
