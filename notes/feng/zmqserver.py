# encoding: UTF-8

from time import sleep, time
from vnrpc import RpcServer
from re import split
import pandas as pd
import numpy as np
from urllib.request import urlopen, Request
import tushare

def update_stock():
    global url2,url3
    stock=tushare.get_stock_basics()
    #s=stock.name
    code=stock.index
    scode=[]
    for value in code:
        
        if value[0]=='6':
            v='sh'+value
            scode.append(v)
        else:
            v='sz'+value
            scode.append(v)
    
    url ='http://qt.gtimg.cn/q='
    codestr=[]
    hangshu=int(len(scode)/60)
    for j in range(hangshu):
        lcode=''
        for i in range(0,60):
            lcode=lcode+scode[i+j*60]+','
        lcode=lcode[: -1]
        codestr=codestr+[lcode]
        
    
    lcode=''
    for i in range(0,len(scode)-hangshu*60):
        lcode=lcode+scode[i+hangshu*60]+','
    lcode=lcode[: -1]
    codestr=codestr+[lcode]
    url2=[]
    for i in range(len(codestr)):   
        url2=url2+[url+codestr[i]]
    
    #更新新浪代码
    url='http://hq.sinajs.cn/list='
    codestr=[]
    hangshu2=int(len(scode)/800)+1
    for j in range(hangshu2):
        lcode=''
        if j<hangshu2-1:
            for i in range(0,800):
                lcode=lcode+scode[i+j*800]+','
            lcode=lcode[: -1]
            codestr=codestr+[lcode]
        else:
            for i in range(j*800,len(scode)):
                lcode=lcode+scode[i]+','
            lcode=lcode[: -1]
            codestr=codestr+[lcode]    
    
    
    url3=[]
    for i in range(len(codestr)):   
        url3=url3+[url+codestr[i]]
def get_sina():
    #decode('gbk')
    ahq=b''
    for i in range(len(url3)):
        request = Request(url3[i])
        text = urlopen(request, timeout=10).read()
        ahq+=text
    m=split(',',ahq.decode('gbk')) 
    m=m[:-1]
    datas=np.array(m).reshape(-1,32) 
    codes=[]
    for i in range(len(datas[:,0])):
        if i==0:
            #codes.append(datas[i,0][11:19])
            codes.append(datas[i,0][13:19])
        else:
            #codes.append(datas[i,0][16:24])
            codes.append(datas[i,0][18:24])
            
    #da=np.hstack((np.array(codes).reshape(len(codes),1),datas[:,1:]))
    hq=pd.DataFrame(datas[:,1:],index=codes,columns=['open','refclose','now','high',
                    'low','bp','sp','vol','amount','bv1','bp1','bv2','bp2','bv3',
                    'bp3','bv4','bp4','bv5','bp5','sv1','sp1','sv2','sp2','sv3',
                    'sp3','sv4','sp4','sv5','sp5','date','time'])
    hq.iloc[:,:29]=hq.iloc[:,:29].astype('float64')
    #hqs=pd.DataFrame(datas[:,1:],index=codes)
    #hqs.loc[:,:28]=hqs.loc[:,:28].astype('float32')

    return hq        
        
def get_tx():
    ahq=b'' 
    for j in range(len(url2)):
        url=url2[j][:19]+str(float(np.random.rand(1)))+url2[j][19:]
        #request = Request(url2[j])
        request = Request(url)
        text = urlopen(request, timeout=10).read()
        ahq+=text        
        data=ahq.decode('GBK')
        m=split('~',data) 
        m=m[:-1]
        datas=np.array(m).reshape(-1,53)
               
        #da=np.hstack((np.array(codes).reshape(len(codes),1),datas[:,1:]))
        das=pd.DataFrame(datas,index=datas[:,2])
        da=das.iloc[:,[5,4,3,33,34,9,19,6,37,10,9,12,11,14,13,16,15,18,17,20,19,22,21,24,23,26,25,28,27,30,30]]

    return da



class TestServer(RpcServer):
    """测试服务器"""

    # ----------------------------------------------------------------------
    def __init__(self, repAddress, pubAddress):
        """Constructor"""
        super(TestServer, self).__init__(repAddress, pubAddress)
'''
        self.register(self.add)
        self.register(self.tick)

    # ----------------------------------------------------------------------
    def add(self, a, b):
        """测试函数"""
        print( 'receiving: %s, %s' % (a, b))
        return a + b
        
    def tick(self,strs):
        #return u"这是测试TICK"+strs
        return time()
'''

if __name__ == '__main__':
    repAddress = 'tcp://*:2014'
    pubAddress = 'tcp://*:0602'
    update_stock()
    ts = TestServer(repAddress, pubAddress)
    ts.start()
    hq=get_sina()
    while 1:
        #content = 'current server time is %s' % time()
        #print( content)
        try:
            t1=time()

            ti=time()
            c=[ti,hq]
            ts.publish(b'sinahq', c)
            t2=time()
            print(3-t2+t1)
            sleep(3-t2+t1)
        except Exception as e:
            print(e)
            sleep(2)