# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :  用时50分钟
https://leetcode-cn.com/problems/triangle/submissions/
"""

import unittest
from typing import List
import numpy as np


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)
        if depth < 2:
            return triangle[0][0]
        dp = self._make_dp(depth)
        dp[0][0] = triangle[0][0]
        # dp[1][0] = triangle[0][0] + triangle[1][0]
        for i in range(1, depth):
            for j in range(i + 1):  # 边界的调整需要手工画图，归纳法推算
                if self._is_on_the_left(i, j):
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif self._is_on_the_right(i, j):
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        ret = min(dp[depth - 1])
        return int(ret)

    def _is_on_the_left(self, i, j):
        return j == 0

    def _is_on_the_right(self, i, j):
        return j == i

    def _make_dp(self, depth):
        ret = []  # 注意数组生成部分的测试用例，特别是边界问题的处理
        for i in range(depth):
            ret.append([0] * (i+1))
        return ret
    # def _make_dp(self, depth):
    #     ret = np.zeros((depth, depth), dtype=int)
    #     return ret


class TestSolution(unittest.TestCase):
    def test_make_dp(self):
        depth = 2
        s = Solution()
        ret = s._make_dp(depth)
        self.assertEqual([[0], [0, 0]], ret)

    def test_minimumTotal(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        s = Solution()
        ret = s.minimumTotal(triangle)
        self.assertEqual(11, ret)

    def test_minimumTotal_2(self):
        # triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        triangle = [[1], [2, 3]]
        s = Solution()
        ret = s.minimumTotal(triangle)
        self.assertEqual(3, ret)


if __name__ == '__main__':
    unittest.main()
