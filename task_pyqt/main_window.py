import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QListWidget, QFrame, QLabel,QLineEdit, QGridLayout, QTextBrowser)
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer, QThread

from task_pyqt.childWindow import *
import customerInfo.customer_opt

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

'''
mainwindow initialized
    create a main window, and then new some widgets to project. 
'''
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initButton()
        #self.initQLineEdit()
        #self.mainDTh = MainDaemonThread()
        #self.mainDTh.start()
        self.initQListWidget_wechatList()
        self.initQListWidget_customerList()
        self.initTextBrowser()
        self.setWindowTitle('myStockAssistant')
        self.setGeometry(320, 100, 1200, 800)
        self.show()

    '''
    initialized a text Browsers, display customer subcripe information.
    '''
    def initTextBrowser(self):
        self.label = QLabel(self)
        self.label.setText("CustomerBrower")
        self.label.move(680, 20)
        self.label.setFont(QFont("0", 16, QFont.Bold))

        self.text_browser = QTextBrowser(self)
        self.text_browser.move(680, 50)
        self.text_browser.resize(500, 700)

    '''
    wechat list initialized, this list be used to select item to customer list
    '''
    def signal_wechatList_doublClicked(self, item):
        print("wechat list double clicked event!")
        pass

    def initQListWidget_wechatList(self):
        listWidget  = QListWidget(self)
        listWidget.move(40, 150)
        listWidget.resize(160, 600)
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        listWidget.itemDoubleClicked.connect(self.signal_wechatList_doublClicked)

    '''
    customer list initialized, customer list include two click event
    customer default information is sh0000001
    clicked: browser customer information
    double clicked: modify subscribe info of customer
    '''
    def signal_customerList_doublClicked(self, item):
        child_win = child_Window(item)
        child_win.show()
        child_win.exec()

    def signal_customerList_clicked(self, item):
        nameBrowser = customerInfo.customer_opt.Customer_info()
        data_brw = nameBrowser.read_StockInfo(item.text())
        if data_brw != '':
            self.text_browser.setText(data_brw)

    def initQListWidget_customerList(self):
        listWidget  = QListWidget(self)
        listWidget.move(230, 150)
        listWidget.resize(160, 600)
        listWidget.addItem("zhangsan")
        listWidget.addItem("lisi")
        listWidget.addItem("wangwu")
        listWidget.addItem("zhaoliu")
        listWidget.itemDoubleClicked.connect(self.signal_customerList_doublClicked)
        listWidget.itemClicked.connect(self.signal_customerList_clicked)  # 绑定点击事件

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

    def closeEvent(self, event):
        print("closeEvent.......")
        print("exit windows.")

    def mousePressEvent(self, event):
        print("mouse press event....")


class MainWindow_task():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


'''
Main function, PyQt5 come ture.
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())



