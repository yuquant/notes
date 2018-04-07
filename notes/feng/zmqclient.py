# encoding: UTF-8

from time import sleep, time
from vnrpc import RpcClient
#from re import split

########################################################################
class TestClient(RpcClient):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, reqAddress, subAddress):
        """Constructor"""
        super(TestClient, self).__init__(reqAddress, subAddress)

    # ----------------------------------------------------------------------
    def callback(self, topic, data):
        global hq
        """回调函数实现"""
        #print ('回调函数测试', topic, ', data:', data)
        #hq=data
        #print(hq[0,0])
        print(time()-data[0])   #float64 df  0.03s

if __name__ == '__main__':
    reqAddress = 'tcp://localhost:2018'
    subAddress = 'tcp://localhost:9888'

    tc = TestClient(reqAddress, subAddress)
    tc.subscribeTopic(b'sinahq')
    tc.start()

    while 1:
        t1=time()
        '''
        t2=tc.tick('shijian')
        t3=time()
        print(t2-t1)
        print(t3-t2)
        print(t3-t1)
        #t=float (tc)-time()
        '''
        sleep(1)