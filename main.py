import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector
from src.lib.connect import *

def actionConnectEvent():
    connect()

app = QApplication(sys.argv)
fen = QMainWindow()
menuBar = QMenuBar(fen)
menuFichier = QMenu()
menuFichier.setTitle("Fichier")
menuConnect = QMenu()
menuConnect.setTitle("Connexions")
menuBar.addMenu(menuFichier)
menuBar.addMenu(menuConnect)
actionConnect = QAction()
actionConnect.setText("Se connecter")
actionConnect.setIcon(QIcon("src/img/connect.png"))
actionDisconnect = QAction()
actionDisconnect.setText("Se déconnecter")
actionDisconnect.setIcon(QIcon("src/img/disconnect.png"))
actionDisconnect.setEnabled(False)
actionConnect.triggered.connect(actionConnectEvent)
menuConnect.addAction(actionConnect)
menuConnect.addAction(actionDisconnect)
centralWidget = QWidget(fen)
gridLayout = QGridLayout(centralWidget)
fen.setCentralWidget(centralWidget)
fen.setLayout(gridLayout)
fen.setMenuBar(menuBar)
fen.showFullScreen()
sys.exit(app.exec_())