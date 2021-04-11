# -*- coding: utf-8 -*-

import requests
import json
import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QDialog, QPushButton
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)
dlg = QDialog()
dlg.setWindowTitle('Python_GUI')
dlg.resize(800, 450)

class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self

dlg.show()
sys.exit(app.exec())