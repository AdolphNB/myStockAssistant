import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QWidget, QPushButton, QListWidget, QFrame, QLabel,QLineEdit, QGridLayout, QTextBrowser)
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer, QThread


class child_Window(QDialog):
    def __init__(self, item):
        super().__init__()
        self.stockSel = "上证(sh999999)"
        self.strategySel = "strategy1"
        self.ctm_stockStrategy = "Target:" + self.stockSel + ' ' + "Model:" + self.strategySel + '\n'
        self.userText = item.text()
        self.setWindowTitle(item.text() + " setting")
        self.resize(760, 510)
        self.initTextBrowser()
        self.initButton_OK()
        self.initButton_cancel()
        self.initQLineEdit_code()
        self.initQLineEdit_idea()
        self.initQListWidget_stockList()
        self.initQListWidget_strategyList()

    '''
    text browser setting
    '''
    def textBrowser_setText(self, stock_str, strategy_str):
        self.ctm_stockStrategy = "Target:" + stock_str + ' ' + "Model:" + strategy_str + '\n'
        self.text_browser.setText(self.ctm_stockStrategy)

    def initTextBrowser(self):
        self.text_browser = QTextBrowser(self)
        self.text_browser.move(40, 20)
        self.text_browser.resize(520, 90)
        self.text_browser.setText(self.ctm_stockStrategy)

    '''
    button event: overwrite close event
    '''
    def store_selData(self):
        str = self.text_browser.toPlainText()
        print(str)
        print("done windows.")
        self.close()

    def initButton_OK(self):
        self.qbtn = QPushButton("OK", self)
        self.qbtn.resize(120, 30)
        self.qbtn.move(600, 20)
        self.qbtn.clicked.connect(self.store_selData)

    def initButton_cancel(self):
        self.qbtn = QPushButton("CANCEL", self)
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

    '''
        stock list configure
    '''
    def signalLW_stockList_clicked(self, item):
        self.stockSel = item.text()
        self.textBrowser_setText(self.stockSel, self.strategySel)

    def initQListWidget_stockList(self):
        listWidget  = QListWidget(self)
        listWidget.move(40, 160)
        listWidget.resize(300, 330)
        listWidget.addItem("中国核电(sh601985)")
        listWidget.addItem("中信证券(sh600030)")
        listWidget.itemClicked.connect(self.signalLW_stockList_clicked)  # 绑定点击事件

    '''
        strategy list configure
    '''
    def signalLW_strategyList_clicked(self, item):
        self.strategySel = item.text()
        self.textBrowser_setText(self.stockSel, self.strategySel)

    def initQListWidget_strategyList(self):
        listWidget = QListWidget(self)
        listWidget.move(420, 160)
        listWidget.resize(300, 330)
        listWidget.addItem("量能异常变化")
        listWidget.addItem("15分钟价格波动")
        listWidget.addItem("小波分析")
        listWidget.addItem("板块波动延迟")
        listWidget.itemClicked.connect(self.signalLW_strategyList_clicked)  # 绑定点击事件


