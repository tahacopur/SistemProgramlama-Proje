import os
import shutil

from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(652, 443)
        self.sirala = QtWidgets.QPushButton(Form)
        self.sirala.setGeometry(QtCore.QRect(20, 400, 181, 26))
        self.sirala.setObjectName(_fromUtf8("sirala"))
        self.gmail = QtWidgets.QPushButton(Form)
        self.gmail.setGeometry(QtCore.QRect(470, 400, 121, 26))
        self.gmail.setObjectName(_fromUtf8("gmail"))
        self.tar = QtWidgets.QPushButton(Form)
        self.tar.setGeometry(QtCore.QRect(260, 400, 151, 26))
        self.tar.setObjectName(_fromUtf8("tar"))
        self.dizin = QtWidgets.QListWidget(Form)
        self.dizin.setGeometry(QtCore.QRect(350, 50, 256, 192))
        self.dizin.setObjectName(_fromUtf8("dizin"))
        self.dosya = QtWidgets.QListWidget(Form)
        self.dosya.setGeometry(QtCore.QRect(30, 50, 256, 192))
        self.dosya.setObjectName(_fromUtf8("dosya"))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 65, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 65, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gonderecek = QtWidgets.QLineEdit(Form)
        self.gonderecek.setGeometry(QtCore.QRect(460, 270, 161, 25))
        self.gonderecek.setObjectName(_fromUtf8("gonderecek"))
        self.gonderilen = QtWidgets.QLineEdit(Form)
        self.gonderilen.setGeometry(QtCore.QRect(460, 330, 161, 25))
        self.gonderilen.setObjectName(_fromUtf8("gonderilen"))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 270, 181, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 330, 181, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit=QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 270, 161, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.sirala.clicked.connect(self.liste)
       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.sirala.setText(_translate("Form", "Dosya Dizin Sırala", None))
        self.gmail.setText(_translate("Form", "Gmail Gönder", None))
        self.tar.setText(_translate("Form", "Dosya TAR yap", None))
        self.label.setText(_translate("Form", "DOSYA", None))
        self.label_2.setText(_translate("Form", "DİZİN", None))
        self.label_3.setText(_translate("Form", "Gönderecek Gmail Adresi :", None))
        self.label_4.setText(_translate("Form", "Gönderilen Gmail Adresi :", None))

    def liste(self):
        a=self.lineEdit.text()
        print(os.listdir(a))
        for i in os.listdir(a):
           dosya = os.path.join(a,i)
           if os.path.isdir(dosya):
             print ('Klasör => ',i)
             self.dizin.addItem(i)
           elif os.path.isfile(dosya):
             print ('Dosya => ',i)
             self.dosya.addItem(i)


