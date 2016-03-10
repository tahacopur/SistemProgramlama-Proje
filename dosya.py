# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dosyamıdizinmi.ui'
#
# Created: Sun Jun 14 23:09:15 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(-10, 10, 141, 111))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 140, 131, 131))
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 30, 161, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 90, 98, 27))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.liste)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
#bir texten yol alıp onun klasor mu dizin mi oldugunu bulup ayrı ayrı listeye atan program

    def liste(self):
        a=self.lineEdit.text()
        print(os.listdir(a))
        for i in os.listdir(a):
           dosya = os.path.join(a,i)
           if os.path.isdir(dosya):
             print ('Klasör => ',i)
             self.listWidget.addItem(i)
           elif os.path.isfile(dosya):
             print ('Dosya => ',i)
             self.listWidget_2.addItem(i)