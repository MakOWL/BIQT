# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTestDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTestDialog(object):
    def setupUi(self, AddTestDialog):
        AddTestDialog.setObjectName("AddTestDialog")
        AddTestDialog.resize(400, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddTestDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AddTestDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(AddTestDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.createButton = QtWidgets.QPushButton(AddTestDialog)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)

        self.retranslateUi(AddTestDialog)
        QtCore.QMetaObject.connectSlotsByName(AddTestDialog)

    def retranslateUi(self, AddTestDialog):
        _translate = QtCore.QCoreApplication.translate
        AddTestDialog.setWindowTitle(_translate("AddTestDialog", "Add Test"))
        self.label.setText(_translate("AddTestDialog", "Enter Test Name:"))
        self.createButton.setText(_translate("AddTestDialog", "Create Test"))
