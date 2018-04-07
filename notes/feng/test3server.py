# encoding: UTF-8

from time import sleep, time

from vnrpc import RpcServer

import pandas as pd

import numpy as np



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

if __name__ == '__main__':
    repAddress = 'tcp://*:2014'
    pubAddress = 'tcp://*:0602'

    ts = TestServer(repAddress, pubAddress)
    ts.start()

    while 1:
        content = 'current server time is %s' % time()
        print content
        x = pd.DataFrame(data=pd.Series([1, 2, 3, 4, 5, 6, 6, 6, 6, 10]), index=np.arange(10))
        ts.publish('test', x)
        sleep(2)