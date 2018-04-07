# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:14:52 2017
pandas numpy 学习
@author: LiuWeipeng
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser = Series(np.arange(3.))

data = DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))
d=len(scode)*600
H5=DataFrame(np.arange(d).reshape(len(scode),600),index=scode)
a=data['w']  #选择表格中的'w'列，使用类字典属性,返回的是Series类型

data.w    #选择表格中的'w'列，使用点属性,返回的是Series类型

data[['w']]  #选择表格中的'w'列，返回的是DataFrame类型

data[['w','z']]  #选择表格中的'w'、'z'列

data[0:2]  #返回第1行到第2行的所有行，前闭后开，包括前不包括后

data[1:2]  #返回第2行，从0计，返回的是单行，通过有前后值的索引形式，
       #如果采用data[1]则报错

data['a':'b']  #利用index值进行切片，返回的是**前闭后闭**的DataFrame, 
        #即末端是包含的  
data.ix[:,[1,2]]  #ix and iloc sometime the same，闭区间
data.ix[1:2,2:4]  #选择第2-3行，3-5（不包括5）列的值

data.iloc[:,[1,2]]
data.iloc[[0,2],[1,2]]
data.iloc[1,0]  #【列数，行数】
data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame

data+=1
data*=2
data2=data*3+10
data4=data2/data
data6=[data,data4]
data6[0].iloc[1,2]  #只能用。loc或者iloc  分别为标签和数字

df1=DataFrame({'A':['A0','A1','A2','A3'],
               'B':['B0','B1','B2','B3'],
               'C':['C0','C1','C2','C3'],
               'D':['D0','D1','D2','D3']},
               index=[0,1,2,3])
df4=DataFrame({'B':['B2','B3','B6','B7'],
               'D':['D2','D3','D6','D7'],
               'F':['F2','F3','F6','F7']},
               index=[2,3,6,7])
jiaoji=pd.concat([df1,df4],axis=1,join='inner')  #交集
bingji=pd.concat([df1,df4],axis=1)  #对齐纵坐标标签 index  可做日期
hebing = pd.concat([df1,df4])      #对齐横坐标标签 columns  可做品种



data.head()  #返回data的前几行数据，默认为前五行，需要前十行则data.head(10)
data.tail()  #返回data的后几行数据，默认为后五行，需要后十行则data.tail(10)
ser[0]
data.loc['a',['w','x']]   #返回‘a’行'w'、'x'列，这种用于选取行索引列索引已知

data.iat[1,0]   #选取第二行第二列，用于已知行、列位置的选取。 【列数，行数】

data = DataFrame(ser)
data.to_csv('data.csv')
data=pd.read_csv('data.csv')
data.columns = list('bcde')



import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = DataFrame(np.arange(15).reshape(3,5),index=['one','two','three'],columns=['a','b','c','d','e'])
data.apply(lambda x:x.max())  #每列的最大值
data.T.apply(lambda x:x.min())  #每行的最大值
data
Out[7]: 
        a   b   c   d   e
one     0   1   2   3   4
two     5   6   7   8   9
three  10  11  12  13  14

#对列的操作方法有如下几种

data['a']
Out[8]: 
one       0
two       5
three    10
Name: a, dtype: int32

data.a
Out[9]: 
one       0
two       5
three    10
Name: a, dtype: int32

data[['a']]
Out[10]: 
        a
one     0
two     5
three  10

data.ix[:,[0,1,2]]  #不知道列名只知道列的位置时
Out[13]: 
        a   b   c
one     0   1   2
two     5   6   7
three  10  11  12

data.ix[1,[0]]  #选择第2行第1列的值
Out[14]: 
a    5
Name: two, dtype: int32

data.ix[[1,2],[0]]   #选择第2,3行第1列的值
Out[15]: 
        a
two     5
three  10

data.ix[1:3,[0,2]]  #选择第2-4行第1、3列的值
Out[17]: 
        a   c
two     5   7
three  10  12

data.ix[1:2,2:4]  #选择第2-3行，3-5（不包括5）列的值
Out[29]: 
     c  d
two  7  8

data.ix[data.a>5,3]  #取data.a>5的元素的列位置
Out[30]: 
three    13
Name: d, dtype: int32

data.ix[data.b>6,3:4]  #选择'b'列中大于6所在的行中的第4列，有点拗口
Out[31]: 
        d
three  13

data.ix[data.a>5,2:4]  #选择'a'列中大于5所在的行中的第3-5（不包括5）列
Out[32]: 
        c   d
three  12  13

data.ix[data.a>5,[2,2,2]]  #选择'a'列中大于5所在的行中的第2列并重复3次
Out[33]: 
        c   c   c
three  12  12  12

#还可以行数或列数跟行名列名混着用
data.ix[1:3,['a','e']]
Out[24]: 
        a   e
two     5   9
three  10  14

data.ix['one':'two',[2,1]]
Out[25]: 
     c  b
one  2  1
two  7  6

data.ix[['one','three'],[2,2]]
Out[26]: 
        c   c
one     2   2
three  12  12

data.ix['one':'three',['a','c']]
Out[27]: 
        a   c
one     0   2
two     5   7
three  10  12

data.ix[['one','one'],['a','e','d','d','d']]
Out[28]: 
     a  e  d  d  d
one  0  4  3  3  3
one  0  4  3  3  3

#对行的操作有如下几种：
data[1:2]  #（不知道列索引时）选择第2行，不能用data[1]，可以用data.ix[1]
Out[18]: 
     a  b  c  d  e
two  5  6  7  8  9


data.ix[1]   #选择第2行
Out[20]: 
a    5
b    6
c    7
d    8
e    9
Name: two, dtype: int32


data['one':'two']  #当用已知的行索引时为前闭后闭区间，这点与切片稍有不同。
Out[22]: 
     a  b  c  d  e
one  0  1  2  3  4
two  5  6  7  8  9

data.ix[1:3]  #选择第2到4行，不包括第4行，即前闭后开区间。
Out[23]: 
        a   b   c   d   e
two     5   6   7   8   9
three  10  11  12  13  14

data.ix[-1:]  #取DataFrame中最后一行，返回的是DataFrame类型,**注意**这种取法是有使用条件的，只有当行索引不是数字索引时才可以使用，否则可以选用`data[-1:]`--返回DataFrame类型或`data.irow(-1)`--返回Series类型
Out[11]: 
        a   b   c   d   e
three  10  11  12  13  14

data[-1:]  #跟上面一样，取DataFrame中最后一行，返回的是DataFrame类型
Out[12]: 
        a   b   c   d   e
three  10  11  12  13  14

data.ix[-1] #取DataFrame中最后一行，返回的是Series类型，这个一样，行索引不能是数字时才可以使用
Out[13]: 
a    10
b    11
c    12
d    13
e    14
Name: three, dtype: int32

data.tail(1)   #返回DataFrame中的最后一行
data.head(1)   #返回DataFrame中的第一行

