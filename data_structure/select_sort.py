# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""

import unittest


class Solution:
    def select_sort(self, nums: list) -> list:
        ret = []
        for _ in range(len(nums)):
            smallest_index = self._find_the_smallest_index(nums)
            ret.append(nums.pop(smallest_index))
        return ret

    def _find_the_smallest_index(self, nums) -> int:
        smallest = nums[0]  # 最大值最小值不需要设置为inf，只需要随便选一个值就行
        smallest_index = 0
        for i, num in enumerate(nums):
            if num < smallest:
                smallest = num
                smallest_index = i
        return smallest_index


class TestSolution(unittest.TestCase):
    def test_select_sort(self):
        a = [8, 5, 7, 8, 9]
        ret = Solution().select_sort(a)
        self.assertEqual(ret, [5, 7, 8, 8, 9])


if __name__ == '__main__':
    unittest.main()
