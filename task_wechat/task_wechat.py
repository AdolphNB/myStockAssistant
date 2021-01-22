#encoding=utf-8
from wxpy import *

bot = Bot(cache_path=True)
bot.file_helper.send("hello zhangqiang")



















'''
import itchat
import time
import random

#itchat.auto_login()
#friends_list = itchat.get_friends(update=True)
itchat.auto_login()
#print(friends_list)
name = itchat.search_friends(name=u'Black')
XiaoMing = name[0]["UserName"]

message_list = [u'Hey,dude', u'Are you ok?', u'Bye~']
message_concent = random.sample(message_list, 1)[0]

while True:
    itchat.send(message_concent, XiaoMing)
    time.sleep(5)
'''



