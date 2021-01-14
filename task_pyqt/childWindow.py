import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QWidget, QPushButton, QListWidget, QFrame, QLabel,QLineEdit, QGridLayout, QTextBrowser)
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer, QThread


class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()  # 子窗口的实例化
        self.child.setupUi(self)


