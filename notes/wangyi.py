# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:59:22 2018

@author: LiuWeipeng
"""
import logging
logger = logging.getLogger('statistic')  
logger.setLevel(logging.DEBUG)  
  
# 创建一个handler，用于写入日志文件  
fh = logging.FileHandler('yhmoni.log')  
fh.setLevel(logging.DEBUG)  
  
# 再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
  
# 定义handler的输出格式  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
# 给logger添加handler  
logger.addHandler(fh)  
logger.addHandler(ch) 

# -*- coding: utf8 -*-
import pandas as pd
import tushare as ts
import requests as req
import json
from time import sleep,time
import re  #(?<=\{)[^}]*(?=\})
alltickers =ts.get_stock_basics()
stocklist = list(alltickers.index.values)
#一次200
ncount=200
stocks=['0'+stock if stock[0:2]=='60' else '1'+stock for stock in stocklist]
heads={

                'Host': 'api.money.126.net',
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
                'Cookie':'__guid=242674514.3632440553501488600.1516885507259.3416; monitor_count=8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Language': 'zh-CN,zh;q=0.8'

}
while 1:
    try:
        t1=time()
        hq={}
        for i in range(0,len(stocks), ncount):
            # 抓网易行情数据接口http://api.money.126.net/data/feed/0601398,1000001,1000881,money.api
            url = 'http://api.money.126.net/data/feed/' + ','.join(stocks[i:i + ncount])+',money.api'
            #url='http://api.money.126.net/data/feed/0601398,1000001,money.api'
            data = req.get(url,headers=heads)
            retdata = data.text
            p = re.compile("(?<=\\().*(?=\\))")
            allresult = p.findall(retdata)
            alldata=json.loads(allresult[0])
            hq.update(alldata)
        
        hqs=pd.DataFrame.from_dict(hq,orient='index')
        hqs.index=hqs.symbol
        t2=time()   
        print(t2-t1)
        sleep(3-t2+t1)
    except Exception as e:
        logger.exception('ERROR:%s' % str(e))  


