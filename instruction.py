# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instruction.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InstructionWindow(object):
    def setupUi(self, InstructionWindow):
        InstructionWindow.setObjectName("InstructionWindow")
        InstructionWindow.resize(545, 468)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InstructionWindow.sizePolicy().hasHeightForWidth())
        InstructionWindow.setSizePolicy(sizePolicy)
        InstructionWindow.setMinimumSize(QtCore.QSize(200, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InstructionWindow.setWindowIcon(icon)
        InstructionWindow.setAutoFillBackground(False)
        InstructionWindow.setStyleSheet("QDailog{\n"
"background-image: url(\'Image/logo01(Faded).jpg\');\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(InstructionWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(InstructionWindow)
        self.label.setGeometry(QtCore.QRect(62, 9, 400, 20))
        self.label.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(InstructionWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 521, 50))
        self.label_3.setMinimumSize(QtCore.QSize(200, 50))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(InstructionWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 521, 50))
        self.label_4.setMinimumSize(QtCore.QSize(200, 50))
        self.label_4.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(InstructionWindow)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 521, 50))
        self.label_5.setMinimumSize(QtCore.QSize(200, 50))
        self.label_5.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(InstructionWindow)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 521, 50))
        self.label_6.setMinimumSize(QtCore.QSize(200, 50))
        self.label_6.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.proceedButton = QtWidgets.QPushButton(InstructionWindow)
        self.proceedButton.setGeometry(QtCore.QRect(135, 260, 391, 50))
        self.proceedButton.setMinimumSize(QtCore.QSize(200, 50))
        self.proceedButton.setMaximumSize(QtCore.QSize(400, 100))
        self.proceedButton.setStyleSheet("\n"
"background-color: #ADD8E6;\n"
"")
        self.proceedButton.setObjectName("proceedButton")
        self.label_2 = QtWidgets.QLabel(InstructionWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 521, 50))
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.proceedButton.raise_()

        self.retranslateUi(InstructionWindow)
        QtCore.QMetaObject.connectSlotsByName(InstructionWindow)

    def retranslateUi(self, InstructionWindow):
        _translate = QtCore.QCoreApplication.translate
        InstructionWindow.setWindowTitle(_translate("InstructionWindow", "Instructions"))
        self.label.setText(_translate("InstructionWindow", "Instructions"))
        self.label_3.setText(_translate("InstructionWindow", "2. To ensure your answer is counted, you must click the \"Submit\" button for each question."))
        self.label_4.setText(_translate("InstructionWindow", "3. Once you submit an answer you cannot change it."))
        self.label_5.setText(_translate("InstructionWindow", "4. so please review your answer carefully before submitting."))
        self.label_6.setText(_translate("InstructionWindow", "5.Your submitted answers will be saved automatically."))
        self.proceedButton.setText(_translate("InstructionWindow", "I have read the instructions and proceed"))
        self.label_2.setText(_translate("InstructionWindow", "1. This test has a time limit. Please keep track of the time."))