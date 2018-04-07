# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:54:26 2017

@author: LiuWeipeng
"""

from ctypes import *
from time import sleep
from itertools import *
import re
api = WinDLL('007000004909.dll')
api.OpenTdx()

sHost = "58.251.9.52".encode("utf-8")
nPort = 7708
sVersion = "6.41".encode("utf-8")
#sBranchID = 34
sBranchID = "0070".encode("utf-8")
sAccountNo = "007000004909".encode("utf-8")
sTradeAccountNo = "7000004909".encode("utf-8")
sPassword = "159632".encode("utf-8")
sTxPassword ="".encode("utf-8")

results=create_string_buffer(1024*1024)
error=create_string_buffer(256)
print ("strat logon....")
client = api.Logon(sHost, nPort, sVersion, sBranchID, sAccountNo, sTradeAccountNo, sPassword, sTxPassword,error)
print ("logon....")
print ("error="+ error.value.decode('gbk'))

print( client)
if client>-1:
    #api.QueryData.argtypes=[c_int,c_int,c_int,c_char_p,c_char_p,c_float,c_int,c_char_p,c_char_p]
    #SendOrder(int ClientID, int Category ,int PriceType,  char* Gddm,  char* Zqdm , float Price, int Quantity,  char* Result, char* ErrInfo);/
    #api.CancelOrder.argtypes=[c_int,c_char_p,c_char_p,c_char_p,c_char_p]
    #0买入 1卖出  2融资买入  3融券卖出   4买券还券   5卖券还款  6现券还券  本地一秒钟11笔，阿里云估计16笔
    api.SendOrder(client,0,0,'A163609078'.encode("utf-8"),'601288'.encode("utf-8"),c_float(30),c_int(100),results,error)  
    api.SendOrder(client,1,0,'0237256996'.encode("utf-8"),'300033'.encode("utf-8"),c_float(50),c_int(100),results,error)
    #交易所ID， 上海1，深圳0(招商证券普通账户深圳是2)
    api.CancelOrder(client,'1'.encode("utf-8"),'79'.encode("utf-8"),results,error)
    api.QueryData(client,0,results,error)  #0资金  1股份 2当日委托  3当日成交  4可撤单 5股东代码  6融资余额  7融券余额  8可融证券
    api.GetQuote(client,'000001'.encode("utf-8"),results, error)
    
    data=re.split('\t', results.value.decode('gbk'))
    print(data)
    print (error.value.decode('gbk'))     
     
api.Logoff(client) 
api.CloseTdx()

'''
2.7
sHost = "58.251.9.52"
nPort = 7708
sVersion = "6.41"
#sBranchID = 34
sBranchID = "0070"
sAccountNo = "007000004909"
sTradeAccountNo = "7000004909"
sPassword = "159632"
sTxPassword =""
'''
'''
3.6批量获取数据，不稳定，总是不完整
import tushare as ts
stocks=ts.get_stock_basics()
#s=stock.name
code=stocks.index
stock=[]
for val in code:
    #stock.append(val.encode("utf-8"))
    stock.append(val)
#QueryDatas(int ClientID, int Category[], int Count, char* Result[], char* ErrInfo[])
def getquotes(ClientID,stock):
    count=80  #130,不是很稳定，经常数据不完整
    
    stocks=(c_char_p * count)()
    info = (c_char_p * count)()
    errors=(c_char_p * count)()
    for i in range(count):
        info[i]='\000'.encode("utf-8")*1024
        stocks[i]=stock[i].encode("utf-8")
        errors[i]='\000'.encode("utf-8")*256

    api.GetQuotes(client,stocks,count,info, errors)    
    data=[]
    for i in range(count):
        data.extend(re.split('\t',info[i].decode('gbk')))
    
    
'''

'''
#2.7
 stocks=(c_char_p * 2)('600213','300259')
  info = (c_char_p * 2)()
  errors=(c_char_p * 2)()
  info[0]='\000'*1024
  info[1]='\000'*1024
  errors[0]='\000'*256
  errors[1]='\000'*256


#api.GetQuotes.argtypes = [c_int, c_char_p *2 , c_int, c_char_p * 2, c_char_p * 2]
#api.GetQuote(client,'000001',results,error)
   # print results.value.decode('gbk')
sleep(2)
api.GetQuotes(client,stocks,2,info, errors)
data1= info[0].decode('gbk')
data2=info[1].decode('gbk')
print data1,data2
rows = re.split(r'[\n]', data1)
for row in rows:
     splitdata=re.split(r'[\t]',row)
     
     
     
if client>-1:
    stock80=[]
    start=time()
    for index,stock in enumerate(stocklist):
        index=index+1
        stock80.append(stock)
        if index % 80 ==0:
            stocks=(c_char_p * 80)()
            info=(c_char_p * 80)()
            errors = (c_char_p * 80)()
            for i in range(0,79):
                stocks[i]=stock80[i]
                info[i]='\000' * 1024
                errors[i]='\000' * 256
            sleep(2)
            stock80 = []
            api.GetQuotes(client, stocks, 79, info, errors)
            # for k in range(0,79):
            #     print info[k].decode('gbk')
                #print errors[k].decode('gbk')


        else:
            stock80.append(stock)
    end = time()

    print str((end-start)*1000)
'''


