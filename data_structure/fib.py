# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
0 1 1 2 3 5 8 ...
0 1 2 3 4 5 6
"""

import unittest


class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    def __init__(self):
        self._memo = dict()

    def fib(self, n):
        if n in self._memo:
            return self._memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        ret = self.fib(n - 1) + self.fib(n - 2)
        if n not in self._memo:
            self._memo[n] = ret
        return ret


class Solution3:
    def fib(self, n):
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


class Solution4:
    def fib(self, n):
        pre = 0
        cur = 1
        for i in range(2, n+1):
            next_ = pre + cur
            pre, cur = cur, next_
        return cur


class TestSolution(unittest.TestCase):
    def test_fib(self):
        s = Solution4()
        self.assertEqual(s.fib(3), 2)
        self.assertEqual(s.fib(5), 5)


if __name__ == '__main__':
    unittest.main()
