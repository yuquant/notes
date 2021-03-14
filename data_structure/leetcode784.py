# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :

https://leetcode-cn.com/problems/letter-case-permutation/
"""

from typing import List
import unittest


class Solution:
    def __init__(self):
        self._ret = []

    def letterCasePermutation(self, S: str) -> List[str]:
        size = len(S)
        level = 0
        self._helper(list(S), size, level)
        return self._ret

    def _helper(self, str_list, size, level):
        if level == size:
            self._ret.append(''.join(str_list))
            return  # 注意return不要丢
        target = str_list[level]
        if target.isalpha():
            str_list[level] = target.lower()
            self._helper(str_list, size, level + 1)
            str_list[level] = target.upper()
            self._helper(str_list, size, level + 1)
        else:  # 注意这种情况不要丢
            self._helper(str_list, size, level + 1)


class TestSolution(unittest.TestCase):
    def testletterCasePermutation(self):
        S = "a1b2"
        solution = Solution()
        ret = solution.letterCasePermutation(S)
        self.assertEqual(["a1b2", "a1B2", "A1b2", "A1B2"], ret)


if __name__ == '__main__':
    unittest.main()
