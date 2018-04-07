# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:36:27 2017
直接运行主程序
@author: LiuWeipeng
"""

#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(5)

def move(func):
    for i in range(2):
        print( "I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print( "all over %s" %ctime())
    sleep(10)
    
    