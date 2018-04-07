# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print('hello')
print("hello")
from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

from time import sleep,time,strptime,mktime,localtime,strftime
timeArray =mktime(strptime(date[1]+tick[1], "%Y%m%d%H:%M:%S"))
timestamp=time()
structtime=localtime(int(timestamp))
strftime('%Y-%m-%d %H:%M:%S',structtime)


from WindPy import w
'''
分钟数据近三年,新股从上市日开始
日内分笔数据近一周，没有成交笔数和买卖方向，有十档委托
'''
w.start()
a=w.wsd("300033.SZ", "close,volume", "2017-07-15", "2017-07-20", "")

c=a.Data
wsddata1=w.wsd("000001.SZ", "open,high,low,close,volume,amt", "2015-11-22", "2015-12-22", "Fill=Previous")
printpy(wsddata1) 
   
d=[[1,3,5],[2,4]]
len(d) #2
len(d[0])  #3
f=d[0][2]

s=[1,2,None,4,None,5]
t=0
for value in s:
    if value is None:
        continue
    t=t+value
    
def atfloat(x):
    try:
        return float(x)
    except:
        return x
    
f=open(path,'w')
try:
    write_to_file(f)
except:
        print ('failed')
else:
        print( 'succ')
finally:
    f.close

import pickle
a = {'name':'Tom','age':22}
with open('text.pkl','wb') as file:
    pickle.dump(a,file)
with open('text.pkl','rb') as file2:
    b = pickle.load(file2)
    
import re
import pandas as pd
stock=pd.read_csv('sz50.xls',encoding="gb18030")
stock=pd.read_excel('sz50.xls')
tick=pd.read_csv(r'D:\Stk_Tick_201705\Stk_Tick\Stk_Tick_2017\Stk_Tick_201705\20170503\SH600000_20170503.csv', usecols=list(range(1,28)),encoding='gbk',parse_dates=True,index_col=1)

holding=stock.values
len(holding)
first=holding[0][0]
sec=holding[1][0]
he=first+sec

ho=re.split('\s+',he)

import pandas as pd
import tushare as ts
stock=ts.get_stock_basics()
s=stock.name
code=stock.index
#解禁股,st股，亏损股
m1=ts.xsg_data(month=11,year=2017)
m2=ts.xsg_data(month=12,year=2017)
m3=ts.xsg_data(month=1,year=2018)
m4=ts.xsg_data(month=2,year=2018)
st=ts.get_st_classified()
nianbao=ts.get_report_data(2016,4)
kui=nianbao.code[nianbao.eps<=0]
hei=pd.concat([m1.code,m2.code,m3.code,st.code,kui],axis=0)
hei.to_excel('hei.xls')
hq.loc[:,:28]=hq.loc[:,:28].astype('float64')
ts.get_concept_classified?? #显示源码

#m3=ts.xsg_data(month=1)
#st股
#实时5+1day
m=ts.get_k_data('399101', ktype='5')
a=m.iloc[-1,1]
b=m.iloc[-1,1]

c=range(0,10,2)
a=(1,2,2,3,2)
a.count(2) #3
b=2 in a
c=[[2,3],[4,7,9]]
c[1].append(0)
d=[2,3]+[0,1]
import numpy as np
a=np.where(dfs[:,5]==0)  #返回位置
dfs[a,:]
f=np.array([2,3])+np.array([0,1])
d.extend([7,8])
d.sort()
d.argsort()
d.sort(reverse=True)
e=np.ones((3,2))
e=e.astype(np.int16)
np.unique(e)
f=np.ones_like(e)
f=np.array(np.arange(24)).reshape((4,6))
np.where(f>5,f,5)  #
f[1,0]==f[1][0]
f[[1,3],[0,2]]
f[[1,3]][:,[0,2]]
f.sum(axis=0)#none 1 0
f.cumsum(0)  #列项累加
f.cumprod(1)  #行向累乘
(f>3).sum()  #大于3的个数
np.intersect1d(e,f)# 公共元素
e.repeat(2)
np.union1d(e,f)  #合体
np.in1d(e,f)  #e的元素是否包含于f
np.setdiff1d(f,e)  #f中与e不同的元素
np.setxor1d(f,e)  #异或
np.save('npf.npz',f)
np.savez('npfile.npz',b=a,c=e,d=f)
g=np.load('npfile.npz')
g['b']
np.dot(f.T,f) #内积
np.ceil(f) #floor log rint四舍五入 cos cosh arccos arccosh 
np.max(f)



g=d[1:5]  #not contain 6
g[2:4]=[5,6]
h=g[2:]  #after second
h=g[-2:-1]  #not contain first
g=g*2
h=g[:: 3]
a=[1,2,3]
b=[4,5,6]
c=[a,b]
a.append(b)
a.extend(b)
a=1
b=2
a,b=b,a+b
def fun1():
    print('3333')
    print('done')
    
c=C5.copy()
#fanzhuan
lcode=lcode[:: -1]
#qiepian
lcode=lcode[: -1]
 # read and save var   
import pickle
a = {'name':'Tom','age':22}
c={'liu':'ji','zheng':'hu'}
d=[a,c]  
#save data
pickle_file=open('savea.pkl','wb')
pickle.dump(d,pickle_file)
#read data
pickle_file=open('savea.pkl','rb')
b=pickle.load(pickle_file)
#moni._OperationThs__copyToClipboard()
zxbz=[1,2,3]
zgyh=[4,5,6]
ths=[7,8,9]
dic={'sz399101':zxbz,'sh600000':zgyh}
dic['sz300033']=ths
data=dic['sz399101']
for key in dic:
    print('key is %s,value is %s'%(key,dic[key]))
    
import os
os.system("cls") 

from time import strftime
print(strftime('%Y-%m-%d %H:%M:%S') )
from time import sleep
from time import clock
t1=clock()
sleep(3)
t2=clock()
t3=t2-t1
print(t3)

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
url = 'http://data.gtimg.cn/flashdata/hushen/4day/sz/sz399101.js'

request = Request('http://qt.gtimg.cn/q=s_sz000858,s_sz002606')
text = urlopen(request, timeout=10).read()
text = text.decode('GBK')

import re
m=re.split('~',text)
p=m[1 :: 3]
v=m[2 :: 3]
fp=p[:: 5]

import tushare as ts

stock=ts.get_zz500s()
code=stock.code


scode=[]
for value in code:
    if value[0]=='6':
        v='sh'+value
        scode.append(v)
    else:
        v='sz'+value
        scode.append(v)

url ='http://qt.gtimg.cn/q='
for c in scode:
    url=url+c+','
url=url[: -1]

from time import clock
t1=clock()
from urllib.request import urlopen, Request

request = Request(url)
text = urlopen(request, timeout=10).read()
text = text.decode('GBK')

import re
m=re.split('~',text)        

t2=clock()
print(t2-t1)

for i in range(2):
    print(eval('you'+str(i))

import matplotlib.pyplot as plt

m=counts
fig = plt.figure(figsize=(11, 8))  
ax = fig.add_subplot(1, 1, 1)
ax.plot(m) 
plt.show()

from config import Config
conf=Config()  
logger=conf.getLog() 
import os
path=os.getcwd()

logger.info('foorbar')  
student="jenny"  
isStaff=True  
logger.info("student=%s,isStaff=%s",student,isStaff)  
logger.info("buy:%d",C[0,-1])  

try:
    t2=clock()
    print(t2-t1)
except Exception as e:
    logger.exception('ERROR:%s,%s' % (path,str(e)))  
    
print(1)


'''
pandas
'''
import pandas as pd
import numpy as np
df1=pd.DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
df2=pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
df.rename(columns=('$a': 'a', '$b': 'b', '$c': 'c', '$d': 'd', '$e': 'e'}, inplace=True) 
df1+df2
df1.add(df,fill_value=0)  #sub,div,mul-/*
f=lambda x:x.max()-x.min()
df1.apply(f,axis=1)
f2=lambda x:'%.2f' %  x
df1.applymap(f2)  #元素级应用
df1['a'].map(f2)
df1.sort_index(axis=1,ascending=False)
df1.sort_index(by='b',ascending=False)
df1.sort_index(by=['b','a'],ascending=False)
df1.rank(axis=1,method='min')  #排名，method=average min max first
df1.index.is_unique
df1.mean(axis=1,skipna=False)
df1.idxmax()  #每列最大数值所在行
df1.describe()
df2.a.cov(df2.b)  #协方差
df2.a.corr(df2.b)  #相关系数
df2.corr()
df2.cov()
df2.isnull()
df2.fillna(0)
df2.dropna(axis=0,how='any')
df2.fillna(method='ffill',axis=0)#bfill用后边的值填充
df2.set_index(['d','e'],drop=False)  #将列设置为index
df2.reset_index()  #上一步的逆过程
obj=pd.Series(['c','a','d','a','a','b'])
u=obj.unique()
obj.value_counts()#频数统计

pd.read_table('x.csv',sep=',',skiprows=[1,3],nrows=10) #sep='\s+'
chunker=pd.read_csv('x.csv',chunksize=1000)
df2.to_csv('a.csv')
folder_father='year2018'
folder_son='month1'
df1.to_hdf('test.h5',folder_father+'/'+folder_son,append=True, complib='zlib', complevel=9)
#append表示如果hdf文件中folder存在是否追加
#complib指文件压缩的类型，complevel指压缩级别
data=pd.read_hdf('test.h5',key='year2018/month1')


'''
时间序列处理
'''

rng=pd.date_range('1/29/2000',periods=6,freq='D')
ts2=pd.Series(np.random.randn(6),index=rng)
ts2.to_period('M')
ts3=ts2.reindex(['a','b'],method='ffill')  #bfill
ts3=ts2.reindex(columns=['a','b'],method='ffill')  #bfill
#ts2.to_timestamp(how='end')




'''
重采样
'''
rng=pd.date_range('1/1/2000',periods=100,freq='D')
ts=pd.Series(np.random.randn(len(rng)),index=rng)
ts.resample('M',how='mean')# how= mean first last medan ohlc max min sum axis=0 fill_method=ffill/bfill 
ts.resample('5min',how='sum',closed='left',label='right',loffset='-1s')


rng=pd.date_range('1/1/2000',periods=12,freq='T')  #min
ts=pd.Series(np.random.randn(len(rng)),index=rng)
m=ts.resample('5min',label='right',closed='left').ohlc()  #默认label,closed为left，导致时间未来函数
o=m.open
#升采样
ts.resample('30S').pad()#  ts.resample('30S').bfill()
tick=pd.read_csv('SZ300403_20170505.csv', usecols=[1,2,3,4,5,6,7,8,9,10],encoding='gbk',parse_dates=True,index_col=1)
a=tick[['成交额','成交量']]
b=tick[['最新价']]
b.plot()
m5=b.resample('5min',label='right',closed='right').ohlc()
m5=m5[:-1]
min5=m5.dropna(axis=0,how='all')  #any,axi=0/1
min5.plot()
import matplotlib.pyplot as plt
plt.show()

tick.loc['2017/05/05 10'][['最新价']].plot()
from datetime import time
tick.at_time(time(11,1))#每天11点1分0秒
tick.between_time(time(11,0),time(11,2)) 
#计时功能 %timeit
min5.rolling(window=5,min_periods=1,center=False).mean()#std,var,min,max,mean,sum
zdf=min5.pct_change()  #涨跌幅
ohlc= zdf['最新价']
c=ohlc.rolling(10).corr()  #相关性系数
bzh=(zdf+1).cumprod()
xgx=zdf.iloc[:,1].rolling(window=10).corr(zdf.iloc[:,2],10)  #收益率的相关性系数


s1=pd.Series(range(3),index=['a','b','c'])
s2=pd.Series(range(4),index=['d','b','c','e'])
s2.drop(['d','b'])
pd.DataFrame({'one':s1,'two':s2})

ts1=pd.Series(np.random.randn(3),index=pd.date_range('2012-6-13',periods=3,freq='W-WED'))
#ts1.resample('B')
spliced.update(data2,overwrite=False)

import pandas_datareader as pdr
pdr.get_data_yahoo('AAPL')

from datetime import datetime
localhour= datetime.now().hour    #isoformat()  year month day minute second

'''
numpy
'''
import numpy as np
arr=np.arange(15)
arr.reshape(3,-1)
arr.shape
ar=arr.reshape(3,-1)
ar.ravel()#去掉shape,ravel('F')
ar1=np.arange(15).reshape(5,-1)
ar2=np.arange(10).reshape(5,-1)
np.concatenate([ar1,ar2],axis=1)  #0
np.hstack((ar1,ar2))  #vstack
ar1.repeat(2,axis=1)#0 1  空
np.tile(ar1,(2,1))
ar1[[0,2,4],[1]]#ar1[[0,2,4]]
ar1+ar1[[0,2,4],[1]]
ar1=np.random.randn(15).reshape(5,-1)
indexer=np.lexsort((ar1[:,1],ar1[:,0]))  #多列排序，先拍第一列小到大，在拍第二列
ar1[indexer]
X=np.matrix(ar2)
X.T   #转置
X.I  #矩阵的逆

e=hqa[np.where((hqa[:,1]>20)*(hqa[:,7]>1000000))]

df=hq[(hq.open>20) & (hq.vol>1000000)]

f=hqa[np.where(hqa[:,0]==21.85)]  #是copy
hqa[0,2]=20
hq.iloc[0,1]=20

hqa[np.where(hqa[:,0]==21.85),2] =30
hq.set_value(hq.open==21.85,'now',30)

#性能相差200-1000倍
hour= datetime.now().hour
mini=datetime.now().minute
week=datetime.now().weekday()
'''
ipython
'''

%cd C:\Users\LiuWeipeng\AnacondaProjects
%run duocelue.py
%bookmark home C:\Users\LiuWeipeng\AnacondaProjects
%cd home
!dir #系统命令
%timeit

#存储
import numpy as np
import h5py
f=h5py.File('record.hdf5','r+')
f=h5py.File('big2.hdf5','a')
arr=np.ones((5,2))
arr.resize((10,))
f['test/yset']=arr #写入数据集
dset=f['myset'] #引用数据集
#m=dset.value
out=dset[...]#读取全部
dset[1:4,1]=2 #修改数据,避免频繁关闭打开的修改，会导致文件偏大,解决方式重新打包   !h5repack big2.hdf5 out.hdf5
dset=f.create_dataset('test1',(10,10))
dset=f.create_dataset('test2',(10,10),dtype=np.complex64)  #类型和大小创建的时候就已经确定
f5=h5py.File('yhindex/StockData5.hdf5','w')
dst5=f5.create_dataset('stock',(4000,2000,4803,25),maxshape=(5000,3000,4803,25),chunks=(1,1,4803,25),dtype=np.float32,compression=9,shuffle=True) 

dset[0:5]=np.arange(5).reshape((5,1))
f.flush()  #将缓存写入硬盘
f.close()  #程序关闭时会自动更新数据
f=h5py.File('big2.hdf5','a')  #w完全重写 r只读 r+对现有文件读写 a读写或者创建 w-不覆盖只创建新文件
with h5py.File('big1.hdf5','w') as f1:   #会覆盖
    f1['big']=bigdata
with h5py.File('big2.hdf5','w') as f2:
    f2.create_dataset('big',data=np.ones((100,1000)),dtype=np.float16)#10^-8   60000
f2=h5py.File('big2.hdf5')
dset=f2['fil']
with dset.astype('float64'):
    out=dset[0,:]
f2.create_dataset('img',data=out) 
f2.pop('img')   
f2.flush()    
img=f2['big'][()]
dset=f2.create_dataset('fil',(3,3),dtype=np.int32,fillvalue=10)   
dset[:,:]=dset[0,:]  #广播，向下全替换为第一行数据
dset[0:2,1:] =np.ones((2,2),dtype=np.int32)*2
dst=f2.create_dataset('4d',shape=(100,80,50,20))
dst[0,...,1].shape
dst[0,0,0,0]    
dst=f.create_dataset('unlimited',(2,2),maxshape=(2,None))    
dst.maxshape
dst.resize((2,5))  #通过这种方式添加数据
dst=f.create_dataset('zip',(1000,1000),compression='gzip')  #压缩
dst=f.create_dataset('ziph',(1000,1000),compression=8,shuffle=True)  #gzip压缩级别0-9，默认4 ,加过滤器dst.compression_opts，压缩率20-95，解压时间慢十倍以上
gru=f.create_group('subgroup')
gru2=gru.create_group('group2')
gru2.name
gru2['xin']=10  #没有该数据集就创建，创建后无法直接覆盖，最好用ceate方式，可设定
dst=gru2['xin']
dst2=f['subgroup/group2/xin']
dst2.file==f

mylist=[] #寻找key
f.visit(mylist.append)
dst=f['ziph']
dst.attrs['title']='third'   #添加特征，特征值不能太长太大
dst.attrs['length']=18
[x for x in dst.attrs]
!h5ls -vlr big2.hdf5 #查看文件信息
!h5repack stockdata.hdf5 stockdata3.hdf5  #重新打包
!h5repack stockdata2.hdf5 stockdata4.hdf5
dst=f.create_dataset('lstr',(100,),dtype=h5py.special_dtype(vlen=str))  #字符串
dst[0]='a'
dst[1]='loveyou2'
data=[str(x) for x in dst[0:4]]

fp=open(r"bankuai.txt")
arr=[]
for lines in fp.readlines():
    lines=lines.replace("\n","")
    arr.append(lines)
fp.close()



