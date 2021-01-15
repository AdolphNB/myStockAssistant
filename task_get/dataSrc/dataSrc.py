'''
Date:2018-02-02
Author: adolphZhang(304633698@qq.com)
This module write for get stock information, you can enter a number to this Class
and then could be get message that what want to get.
'''
import sys
import re
import time
import threading
from urllib.request import urlopen


class StockInfo():

    def __init__(self, values='600550'):
        self.stockNumber = values
        html = urlopen('http://hq.sinajs.cn/list=sh%s' % self.stockNumber)
        self.cBuffer = html.read().decode('gbk')
        self.buff = self.cBuffer.split(",")
        self.ThreadCtrl = False
        '''Must use daemon thread, if not, main thread exit, this this thread will
        continue running.'''
        self.thrd = threading.Thread(target=self.postValue, daemon=True).start()

    def postValue(self):
        while True:
            if self.ThreadCtrl == True:
                html = urlopen('http://hq.sinajs.cn/list=sh%s' % self.stockNumber)
                self.cBuffer = html.read().decode('gbk')
                self.buff = self.cBuffer.split(",")
                # print(self.buff)
            time.sleep(2)

    def resetStockNumber(self, values):
        self.stockNumber = values

    def setPostStatus(self, opt):
        self.ThreadCtrl = opt

    def getNumber(self):
        numBuf = re.findall(r'var hq_str_(.*)=', self.buff[0], re.S | re.M)
        return numBuf[0]

    def getName(self):
        numName = re.findall(r'="(.*)', self.buff[0], re.S | re.M)
        return numName[0]

    def getOpenPrice(self):
        return self.buff[1]

    def getLastClosingPrice(self):
        return self.buff[2]

    def getCurrentPrice(self):
        return self.buff[3]

    def getHighestPrice(self):
        return self.buff[4]

    def getLowestPrice(self):
        return self.buff[5]

    def getCurrentBuy1(self):
        return self.buff[6]

    def getCurrentSale1(self):
        return self.buff[7]

    def getCurrentVolume(self):
        return self.buff[8]

    def getCurrentYield(self):
        return self.buff[9]


'''
The following script to use for the test.
Python pass argvment need import sys, and the paraments be stored to sys.argv[].
'''
if __name__ == '__main__':

    if (len(sys.argv) < 2):
        print("U must add a stock number to argv[1], like# python StockInfo.py 600550")
        print("Current parament list is: ")
        print(sys.argv)
        exit()

    stc = StockInfo(sys.argv[1])

    while True:
        print(stc.getName())
        print(stc.getNumber())
        print(stc.getOpenPrice())
        print(stc.getLastClosingPrice())
        print(stc.getCurrentPrice())
        print(stc.getHighestPrice())
        print(stc.getLowestPrice())
        print(stc.getCurrentBuy1())
        print(stc.getCurrentSale1())
        print(stc.getCurrentVolume())
        print(stc.getCurrentYield())
        time.sleep(5)



'''
# -*- coding: utf-8 -*-
import requests
import time as time_sleep
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
'''
'''
Get stock data from internet
    股票数据API整理: https://blog.csdn.net/xp5xp6/article/details/53121481?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-2.control
    1. from sina  :http://hq.sinajs.cn/list=sh601006
        ref: 实时股票数据接口: https://blog.csdn.net/nalnait/article/details/86677286
    2. from yahoo
    3. from tushare
    4. from 
'''
'''
class DataSrc():
    pass


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  # 'utf-8' #
        return r.text
    except:
        return " "

def getData(data):
    data = data.split(',')
    # name = data[0]
    todayOpen = data[1]
    yesterdayClose = data[2]
    nowPrice = data[3]
    todayHigh = data[4]
    todayLow = data[5]

    bidPrice = data[6]
    askPrice = data[7]
    quantity = data[8]
    money = data[9]

    buy1Volume = data[10]
    buy1Price = data[11]
    buy2Volume = data[12]
    buy2Price = data[13]
    buy3Volume = data[14]
    buy3Price = data[15]
    buy4Volume = data[16]
    buy4Price = data[17]
    buy5Volume = data[18]
    buy5Price = data[19]

    sell1Volume = data[20]
    sell1Price = data[21]
    sell2Volume = data[22]
    sell2Price = data[23]
    sell3Volume = data[24]
    sell3Price = data[25]
    sell4Volume = data[26]
    sell4Price = data[27]
    sell5Volume = data[28]
    sell5Price = data[29]

    date = data[30]
    time = data[31]

    data = {'todayOpen': todayOpen, 'yesterdayClose': yesterdayClose, 'nowPrice': nowPrice, 'todayHigh': todayHigh,
            'todayLow': todayLow, 'bidPrice': bidPrice, 'askPrice': askPrice, 'quantity': quantity, 'money': money,
            'buy1Volume': buy1Volume, 'buy1Price': buy1Price, 'buy2Volume': buy2Volume, 'buy2Price': buy2Price,
            'buy3Volume': buy3Volume, 'buy3Price': buy3Price, 'buy4Volume': buy4Volume, 'buy4Price': buy4Price,
            'buy5Volume': buy5Volume, 'buy5Price': buy5Price, 'sell1Volume': sell1Volume, 'sell1Price': sell1Price,
            'sell2Volume': sell2Volume, 'sell2Price': sell2Price, 'sell3Volume': sell3Volume, 'sell3Price': sell3Price,
            'sell4Volume': sell4Volume, 'sell4Price': sell4Price, 'sell5Volume': sell5Volume, 'sell5Price': sell5Price,
            'date': date, 'time': time}
    return data


code = r'sh510900'
url = 'http://hq.sinajs.cn/list=' + code
data = getHTMLText(url)
print(data)

'''
'''
def main():
    code = r'sh510900'
    url = 'http://hq.sinajs.cn/list=' + code
    store_time = list()
    store_price = list()
    fig = plt.figure(figsize=(15, 5))
    ax = fig.add_subplot(1,1,1)
    plt.xlim((datetime(2018, 1, 5, 13, 00), datetime(2018, 1, 5, 15, 31)))
    while True:
        data = getHTMLText(url)
        data = getData(data)
        time = data['time']
        nowPrice = float(data['nowPrice'])
        store_time.append(time)
        store_price.append(nowPrice)
        Price = pd.DataFrame(store_price, index=store_time, columns=['price'])
        Price.index = Price.index.to_datetime()
        index = list(Price.index)
        if len(index) > 5:
            # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M:%S'))
            # plt.xlim((datetime(2017, 1, 5, 9, 30), datetime(2017, 1, 5, 15, 31)))
            ax.plot(index[len(index) - 30:len(index) - 1:1], store_price[len(index) - 30:len(index) - 1:1])
            # plt.set_title("%s" % code)
            plt.pause(0.01)

        time_sleep.sleep(1)
        #print data['time'], data['nowPrice']


main()
'''
