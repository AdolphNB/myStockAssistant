import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QWidget, QPushButton, QListWidget, QFrame, QLabel,QLineEdit, QGridLayout, QTextBrowser)
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer, QThread


class child_Window(QDialog):
    def __init__(self, item):
        super().__init__()
        self.userText = item.text() + " setting"
        self.setWindowTitle(self.userText)
        self.resize(760, 510)
        self.initTextBrowser()
        self.initButton_OK()
        self.initButton_cancel()
        self.initQLineEdit_code()
        self.initQLineEdit_idea()
        self.initQListWidget_stockList()
        self.initQListWidget_strategyList()

    def initTextBrowser(self):
        self.text_browser = QTextBrowser(self)
        self.text_browser.move(40, 20)
        self.text_browser.resize(520, 90)
        self.text_browser.setText("<font color='red'>Hello World</font>")

    '''
    button event: overwrite close event
    '''
    def closeEvent(self, event):
        print(event)
        print("exit windows.")

    def initButton_OK(self):
        self.qbtn = QPushButton("OK", self)
        self.status = False
        self.qbtn.resize(120, 30)
        self.qbtn.move(600, 20)
        self.qbtn.clicked.connect(self.close)

    def initButton_cancel(self):
        self.qbtn = QPushButton("CANCEL", self)
        self.status = False
        self.qbtn.resize(120, 30)
        self.qbtn.move(600, 70)
        self.qbtn.clicked.connect(self.close)

    def initQLineEdit_code(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(40, 130)
        self.lineEdit.resize(300, 30)
        #self.lineEdit.setText('600550')

    def initQLineEdit_idea(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(420, 130)
        self.lineEdit.resize(300, 30)
        #self.lineEdit.setText('600550')

    def initQListWidget_stockList(self):
        listWidget  = QListWidget(self)
        listWidget.move(40, 160)
        listWidget.resize(300, 330)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        #listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件

    def initQListWidget_strategyList(self):
        listWidget = QListWidget(self)
        listWidget.move(420, 160)
        listWidget.resize(300, 330)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        #listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件


