import sys, os
import csv
import pandas as pd

class Customer_info():

    def __init__(self):
        self.pwdPath = os.getcwd()

    def addStockInfo(self, wechatName, selInfo):
        self.name = wechatName + ".csv"
        file_storeName = self.pwdPath + "\\customerInfo\\subscriper_cfg\\"  + self.name
        with open(file_storeName, 'a', encoding='utf-8', newline='') as w:
            csv_writer = csv.writer(w, dialect = 'excel')
            csv_writer.writerow(selInfo)

    def delStockInfo(self, wechatName, selInfo):
        self.name = wechatName + ".csv"
        file_storeName = self.pwdPath + "\\customerInfo\\subscriper_cfg\\"  + self.name
        with open(file_storeName, 'a', encoding='utf-8', newline='') as w:
            w.write(selInfo)

    def modifyStockInfo(self, wechatName, selInfo):
        self.name = wechatName + ".csv"
        file_storeName = self.pwdPath + "\\customerInfo\\subscriper_cfg\\"  + self.name
        with open(file_storeName, 'a', encoding='utf-8', newline='') as w:
            w.write(selInfo)

    def delUserFromList(self, wechatName, selInfo):
        self.name = wechatName + ".csv"
        file_storeName = self.pwdPath + "\\customerInfo\\subscriper_cfg\\"  + self.name
        with open(file_storeName, 'a', encoding='utf-8', newline='') as w:
            w.write(selInfo)

    def read_StockInfo(self, name):
        self.name = name + ".csv"
        file_storeName = self.pwdPath + "\\customerInfo\\subscriper_cfg\\" + self.name
        if not os.path.exists(file_storeName):
            print("file isn't exist!")
            return
        with open(file_storeName, 'r', encoding='utf-8') as file:
            context = file.read()
            return context

    def readAllStockInfo(self):
        pass

    def getTxList(self):
        pass



'''
1.读取CSV文件到List
def readCSV2List(filePath):
    try:
        file=open(filePath,'r',encoding="gbk")# 读取以utf-8
        context = file.read() # 读取成str
        list_result=context.split("\n")#  以回车符\n分割成单独的行
        #每一行的各个元素是以【,】分割的，因此可以
        length=len(list_result)
        for i in range(length):
            list_result[i]=list_result[i].split(",")
        return list_result
    except Exception :
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();# 操作完成一定要关闭
        
2.将List写入到CSV文件中
def writeList2CSV(myList,filePath):
    try:
        file=open(filePath,'w')
        for items in myList:
            for item in items:
                file.write(item)
                file.write(",")
            file.write("\n") 
    except Exception :
        print("数据写入失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();# 操作完成一定要关闭

'''
