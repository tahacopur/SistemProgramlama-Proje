# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sıkıstırma.ui'
#
# Created: Sat Jun 13 18:01:05 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.sikistir = QtWidgets.QPushButton(Form)
        self.sikistir.setGeometry(QtCore.QRect(60, 130, 98, 27))
        self.sikistir.setObjectName("sikistir")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.dosyaal = QtWidgets.QPushButton(Form)
        self.dosyaal.setGeometry(QtCore.QRect(210, 130, 98, 27))
        self.dosyaal.setObjectName("dosyaal")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.dosyaal.clicked.connect(self.dosyal)
        self.sikistir.clicked.connect(self.abcx)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sikistir.setText(_translate("Form", "sıkıstır"))
        self.dosyaal.setText(_translate("Form", "dosyaal"))
    global dosyayolu
    def dosyal(self):
        dosyayolu=QFileDialog.getOpenFileName()[0]
        print(dosyayolu)
        shutil.make_archive(self.lineEdit.text(),'tar',dosyayolu)
    def abcx(self):
        shutil.make_archive('/home/taha/aaaa','tar',dosyayolu)