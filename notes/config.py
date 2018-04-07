# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:44:41 2017

@author: LiuWeipeng
"""

import logging  
class Config():  
    # 创建一个logger  
    logger = logging.getLogger('statistic')  
    logger.setLevel(logging.DEBUG)  
  
    # 创建一个handler，用于写入日志文件  
    fh = logging.FileHandler('tradinglog.log')  
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
    def getLog(self):  
        return self.logger  