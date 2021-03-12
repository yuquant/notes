# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :  单例模式中，init仍然会在实例化时候调用
"""
import unittest


class Log:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            # 创建实例
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name


class TestLog(unittest.TestCase):
    def test_init(self):
        logger_a = Log('a')
        logger_b = Log('b')
        self.assertEqual(logger_a.name, 'b')
        self.assertEqual(logger_b.name, 'b')


if __name__ == "__main__":
    unittest.main()
