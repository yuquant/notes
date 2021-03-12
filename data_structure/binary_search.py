# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
主要复杂在边界处理问题，稍不注意就会陷入死循环
"""

import unittest


class Solution:
    """
    边界逻辑混乱，不推荐
    """

    def binary_search(self, ordered_nums: list, target) -> int:
        start_index = 0
        end_index = len(ordered_nums)

        while True:
            if end_index == 0:
                return -1
            mid_index = (start_index + end_index) // 2
            mid_value = ordered_nums[mid_index]
            if start_index >= end_index:
                return -1
            if target < mid_value:
                end_index = mid_index
            elif target > mid_value:
                start_index = mid_index + 1
            elif target == mid_value:
                return mid_index


# recommended
class Solution2:
    def binary_search(self, ordered_nums: list, target) -> int:
        low = 0
        high = len(ordered_nums) - 1  # 避免超出索引，且空数组直接为-1，不满足while循环条件
        while low <= high:  # 终止条件，当两者相等，mid=low=high
            mid = (low + high) // 2
            guess = ordered_nums[mid]
            if guess == target:
                return mid
            elif target < guess:
                high = mid - 1  # target在mid左侧，且不包含mid
            else:
                low = mid + 1  # mid已经被排除，所以不需要包含，直接移位，如果不移位，则在检索不包含该数字时，无限循环，low和high相差1的位置
        return -1


class TestSolution(unittest.TestCase):
    def test_binary_search_odd(self):
        ordered_nums = [1, 3, 5, 7, 9]
        solution = Solution2()
        ret = solution.binary_search(ordered_nums, 5)
        self.assertEqual(ret, 2)
        ret = solution.binary_search(ordered_nums, 2)
        self.assertEqual(ret, -1)
        ret = solution.binary_search(ordered_nums, 9)
        self.assertEqual(ret, 4)

    def test_binary_search_even(self):
        ordered_nums = [1, 3, 5, 7, 9, 10]
        solution = Solution2()
        ret = solution.binary_search(ordered_nums, 5)
        self.assertEqual(ret, 2)
        ret = solution.binary_search(ordered_nums, 2)
        self.assertEqual(ret, -1)
        ret = solution.binary_search(ordered_nums, 9)
        self.assertEqual(ret, 4)

    def test_binary_search_single(self):
        ordered_nums = [9]
        solution = Solution2()
        ret = solution.binary_search(ordered_nums, 5)
        self.assertEqual(ret, -1)
        ret = solution.binary_search(ordered_nums, 2)
        self.assertEqual(ret, -1)
        ret = solution.binary_search(ordered_nums, 9)
        self.assertEqual(ret, 0)

    def test_binary_search_empty(self):
        ordered_nums = []
        solution = Solution2()
        ret = solution.binary_search(ordered_nums, 5)
        self.assertEqual(ret, -1)
        ret = solution.binary_search(ordered_nums, 2)
        self.assertEqual(ret, -1)
        ret = solution.binary_search(ordered_nums, 9)
        self.assertEqual(ret, -1)


if __name__ == '__main__':
    unittest.main()
