import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector

class connect:
    def __init__(self):
        self.dlg = QDialog()
        self.dlg.resize(480, 271)
        #self.dlg.setWindowFlag(Qt.FramelessWindowHint)
        self.label = QtWidgets.QLabel(self.dlg)
        self.label.setGeometry(QtCore.QRect(185, 9, 110, 109))
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap("src/img/connect.png"))
        self.lineEdit = QtWidgets.QLineEdit(self.dlg)
        self.lineEdit.setGeometry(QtCore.QRect(10, 140, 461, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dlg)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 180, 461, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.dlg)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 461, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Se connecter")
        self.pushButton.clicked.connect(self.login)
        self.lineEdit.setPlaceholderText("Nom d'utilisateur")
        self.lineEdit_2.setPlaceholderText("Mot de passe")
        self.pushButton.setShortcut("Return")
        self.dlg.exec()

    def login(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="python",
                password="python",
                port='3311'
            )
            print("OK")
        except:
            pass
