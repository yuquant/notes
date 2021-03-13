# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
滑动窗口问题， 嵌套循环
"""


import unittest


class Solution:
    def unique(self, lists: list) -> list:
        size = len(lists)
        poped = 0
        for i in range(size):
            index = i - poped  # 删除元素后的偏移纠正
            if self._find(lists[:index], lists[index]) > -1:
                lists.pop(index)
                poped += 1
        return lists

    def _find(self, lists, alpha):
        for i, s in enumerate(lists):
            if s == alpha:
                return i
        return -1


class TestSolution(unittest.TestCase):
    def test_unique(self):
        s1 = 'assdfadd'
        solution = Solution()
        self.assertEqual(solution.unique(list(s1)), list('asdf'))


if __name__ == '__main__':
    unittest.main()
