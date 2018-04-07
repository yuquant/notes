# encoding: UTF-8

from time import sleep, time

from vnrpc import RpcServer

import pandas as pd

import numpy as np

# encoding: UTF-8
# encoding: UTF-8
import requests as req
import tushare as tss
from time import time,sleep,strptime
import pandas as pd

EMPTY_STRING = ''
EMPTY_UNICODE = u''
EMPTY_INT = 0
EMPTY_FLOAT = 0.0
class tickdata(object):

    # ----------------------------------------------------------------------
    def __init__(self):


        # 代码相关
        self.symbol = EMPTY_STRING  # 合约代码
        self.name = EMPTY_STRING
        self.exchange = EMPTY_STRING  # 交易所代码
        self.vtSymbol = EMPTY_STRING  # 合约在vt系统中的唯一代码，通常是 合约代码.交易所代码

        # 成交数据
        self.lastPrice = EMPTY_FLOAT  # 最新成交价
        self.lastVolume = EMPTY_INT  # 最新成交量
        self.volume = EMPTY_INT  # 今天总成交量
        self.openInterest = EMPTY_INT  # 持仓量
        self.time = EMPTY_STRING  # 时间 11:20:56.5
        self.date = EMPTY_STRING  # 日期 20151009
        self.datetime = None  # python的datetime时间对象

        # 常规行情
        self.openPrice = EMPTY_FLOAT  # 今日开盘价
        self.highPrice = EMPTY_FLOAT  # 今日最高价
        self.lowPrice = EMPTY_FLOAT  # 今日最低价
        self.preClosePrice = EMPTY_FLOAT
        self.amount =EMPTY_FLOAT #成交金额

        self.upperLimit = EMPTY_FLOAT  # 涨停价
        self.lowerLimit = EMPTY_FLOAT  # 跌停价

        # 五档行情
        self.bidPrice1 = EMPTY_FLOAT
        self.bidPrice2 = EMPTY_FLOAT
        self.bidPrice3 = EMPTY_FLOAT
        self.bidPrice4 = EMPTY_FLOAT
        self.bidPrice5 = EMPTY_FLOAT

        self.askPrice1 = EMPTY_FLOAT
        self.askPrice2 = EMPTY_FLOAT
        self.askPrice3 = EMPTY_FLOAT
        self.askPrice4 = EMPTY_FLOAT
        self.askPrice5 = EMPTY_FLOAT

        self.bidVolume1 = EMPTY_INT
        self.bidVolume2 = EMPTY_INT
        self.bidVolume3 = EMPTY_INT
        self.bidVolume4 = EMPTY_INT
        self.bidVolume5 = EMPTY_INT

        self.askVolume1 = EMPTY_INT
        self.askVolume2 = EMPTY_INT
        self.askVolume3 = EMPTY_INT
        self.askVolume4 = EMPTY_INT
        self.askVolume5 = EMPTY_INT




        # store = pd.read_hdf('tickdata.h5', 'tick')
        # print store
        # datapd.to_hdf('tickdata4.h5', 'tick', format = 'table',append=True, mode='a')


        # #print data.shape
        # xx=[dataapi,datapd]
        # tt=pd.concat(xx,axis=0)
        # print datapd.shape
        # #dataapi=tt
        # print dataapi.tail(20)
        # sleep(3)


        # for a,b in  tt.groupby(['symbol']):
        #     kk+=1




########################################################################
class TestServer(RpcServer):
    """测试服务器"""

    # ----------------------------------------------------------------------
    def __init__(self, repAddress, pubAddress):
        """Constructor"""
        super(TestServer, self).__init__(repAddress, pubAddress)

        self.register(self.add)
        self.register(self.tick)

    # ----------------------------------------------------------------------
    def add(self, a, b):
        """测试函数"""
        print 'receiving: %s, %s' % (a, b)
        return a + b
    def tick(self,strs):
        return u"这是测试TICK"+strs

    def getsinadata(self):
        alltickers = tss.get_stock_basics()
        stocklist = list(alltickers.index.values)
        ncount = 799
        stocks = ['sh' + stock if stock[0:2] == '60' else 'sz' + stock for stock in stocklist]

        dataapi = pd.DataFrame()
        while True:
            datadetail = []
            tickdatas = []
            start = time()
            for i in range(0, len(stocks), ncount):
                # 抓新浪行情数据接口
                url = 'http://hq.sinajs.cn/list=' + ','.join(stocks[i:i + ncount])
                data = req.get(url)
                retdata = data.text
                rowdata = retdata.split(';')
                for row in rowdata:
                    datadetail.append(row)
                    # 格式化接口
            for rowtick in datadetail:
                rowtick = rowtick.split('"')
                if len(rowtick) == 1:
                    continue
                if rowtick[1] == "":
                    continue
                rowtick = rowtick[1]
                rowtick = rowtick.split(',')
                tick = tickdata()
                tick.symbol = str(rowtick[0].encode('gbk'))
                tick.openPrice = float(rowtick[1])
                tick.preClosePrice = float(rowtick[2])
                tick.lastPrice = float(rowtick[3])
                tick.highPrice = float(rowtick[4])
                tick.lowPrice = float(rowtick[5])
                tick.askPrice1 = float(rowtick[6])
                tick.bidPrice1 = float(rowtick[7])
                tick.volume = float(rowtick[8])
                tick.amount = float(rowtick[9])
                tick.askVolume1, tick.askPrice1, tick.askVolume2, tick.askPrice2, tick.askVolume3, tick.askPrice3, tick.askVolume4, tick.askPrice4, tick.askVolume5, tick.askPrice5 = [
                    float(x) for x in rowtick[10:20]]
                tick.bidVolume1, tick.bidPrice1, tick.bidVolume2, tick.bidPrice2, tick.bidVolume3, tick.bidPrice3, tick.bidVolume4, tick.bidPrice4, tick.bidVolume5, tick.bidPrice5 = [
                    float(x) for x in rowtick[20:30]]
                tick.date = str(rowtick[30])
                tick.time = str(rowtick[31])
                tickdatas.append(tick.__dict__)
            datapd = pd.DataFrame.from_dict(tickdatas)
            datapd.set_index('time', inplace=True)
            datapd = datapd[datapd['openPrice'] <> 0]
            end = time()
            return datapd
            print (end - start) * 1000
            sleep(3)

if __name__ == '__main__':
    repAddress = 'tcp://*:2014'
    pubAddress = 'tcp://*:0602'

    ts = TestServer(repAddress, pubAddress)
    ts.start()

    while 1:
        content = 'current server time is %s' % time()
        print content
        data=ts.getsinadata()
        ts.publish('test', data)
        #x = pd.DataFrame(data=pd.Series([1, 2, 3, 4, 5, 6, 6, 6, 6, 10]), index=np.arange(10))


        sleep(1)