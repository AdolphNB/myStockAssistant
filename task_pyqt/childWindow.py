import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QWidget, QPushButton, QListWidget, QFrame, QLabel,QLineEdit, QGridLayout, QTextBrowser)
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer, QThread


class child_Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("customer_setting")
        self.initQListWidget_stockList()
        self.resize(800, 500)
        #self.initQListWidget_strategyList()


    def initQListWidget_stockList(self):
        listWidget  = QListWidget(self)
        listWidget.move(50, 50)
        listWidget.resize(160, 300)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        #listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件

    def initQListWidget_strategyList(self):
        listWidget  = QListWidget(self)
        #listWidget.move(730, 150)
        #listWidget.resize(160, 600)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        #listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件


