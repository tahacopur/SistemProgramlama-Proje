# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gmailat.ui'
#
# Created: Sat Jun 13 16:36:40 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
import email.utils
from email.mime.text import MIMEText
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 113, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gonder = QtWidgets.QPushButton(Form)
        self.gonder.setGeometry(QtCore.QRect(220, 40, 98, 27))
        self.gonder.setObjectName("gonder")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 130, 113, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.gonder.clicked.connect(self.yolla)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gonder.setText(_translate("Form", "gonder"))

    def yolla(self):

     msg =MIMEText("Son Uyarı") # MIMEText calss'ından bir nesne üretiliyor. Burada parametre olarak
#mesaj içerisine yazılacak metin veriliyor.
     msg['To'] =  self.lineEdit.text() #mailin kime gönderileceği belirleniyor
     msg['From'] = self.lineEdit_2.text() # mailin kimden gönderileceği belirleniyor
     msg['Subject'] = self.lineEdit_3.text() #mesajın konusu belirleniyor

     server = smtplib.SMTP('')# bu kısım bir önceki örnekle aynı
     server.set_debuglevel(True)# bu fonksiyon yardımı ile mail gönderme işlemindeki her mesaj alışverişinin
#listelenmesi sağlanıyor.
     server.starttls()#bu kısım bir önceki örnekle aynı
     server.login("","")#bu kısım bir önceki örnekle aynı
     try:
        server.sendmail(msg['From'], msg['To'], msg.as_string())#bu kısım bir önceki örnekle aynı
     except:
         print("email yanliş gönderilmedi")
     finally:
          server.quit()#bu kısım bir önceki örnekle aynı