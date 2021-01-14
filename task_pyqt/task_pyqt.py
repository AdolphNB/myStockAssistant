import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QListWidget, QFrame, QLabel,QLineEdit, QGridLayout, QTextBrowser)
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer, QThread


class MainDaemonThread(QThread):
    def __init__(self):
        super().__init__()
        self.srcData = 0
        self.dataOpt = 0

    def run(self):
        while True:
            if self.srcData <= self.dataOpt:
                print("Thread>>>>")
            time.sleep(1)

    def compareValue(srcData, datOpt):
        self.srcData = srcData
        self.dataOpt = datOpt



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initButton()
        self.initQLineEdit()
        #self.mainDTh = MainDaemonThread()
        #self.mainDTh.start()
        self.initQListWidget_wechatList()
        self.initQListWidget_customerList()
        self.initTextBrowser()
        #self.initQListWidget_strategyList()
        #self.initQListWidget_stockList()
        self.setWindowTitle('myStockAssistant')
        self.setGeometry(100, 100, 1200, 800)
        self.show()

    def initTextBrowser(self):
        self.label = QLabel(self)
        self.label.setText("CustomerBrower")
        self.label.move(680, 20)
        self.label.setFont(QFont("0", 16, QFont.Bold))

        self.text_browser = QTextBrowser(self)
        self.text_browser.move(680, 50)
        self.text_browser.resize(500, 700)
        self.text_browser.setText("<font color='red'>Hello World</font>")

    def initQListWidget_wechatList(self):
        listWidget  = QListWidget(self)
        listWidget.move(40, 150)
        listWidget.resize(160, 600)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件

    def initQListWidget_customerList(self):
        listWidget  = QListWidget(self)
        listWidget.move(230, 150)
        listWidget.resize(160, 600)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件

    '''
    def initQListWidget_stockList(self):
        listWidget  = QListWidget(self)
        listWidget.move(500, 150)
        listWidget.resize(160, 600)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件

    def initQListWidget_strategyList(self):
        listWidget  = QListWidget(self)
        listWidget.move(730, 150)
        listWidget.resize(160, 600)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        listWidget.itemClicked.connect(self.signalListWidget_clicked)  # 绑定点击事件
    '''

    def initQLineEdit(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(10, 100)
        self.lineEdit.setText('600550')

    # this button is a flag that start/stop stock-data update by press or release it.
    def initButton(self):
        self.qbtn = QPushButton("START", self)
        self.status = False
        self.qbtn.clicked.connect(self.signalBtn_START_STOP)
        self.qbtn.move(10, 30)

    # this method is a SIGNAL-response callback method, initialize method see initButton()
    def signalBtn_START_STOP(self):
        if self.status == False:
            self.status = True
            self.stock.setPostStatus(True)
            self.qbtn.setText("STOP")
            self.stock.resetStockNumber(self.lineEdit.text())
            # print("START")
        else:
            self.status = False
            self.stock.setPostStatus(False)
            self.qbtn.setText("START")
            # print("STOP")

    def signalListWidget_clicked(self, item):
        print("qlistwidget click")

    def operate(self):
        buf = self.stock.getCurrentPrice()
        self.label.setText(buf)

    def closeEvent(self, event):
        print("closeEvent.......")
        print("exit windows.")

    def mousePressEvent(self, event):
        print("mouse press event....")

'''
Main function, PyQt5 come ture.
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())



