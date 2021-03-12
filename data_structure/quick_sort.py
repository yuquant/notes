# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""

import unittest


class Solution:
    def quick_sort(self, nums: list) -> list:

        if len(nums) <= 1:  # 有时候nums会为空数组
            return nums
        else:

            mid_index = 0
            mid = nums[mid_index]
            less = []
            greater = []
            for n in nums[1:]:
                if n <= mid:
                    less.append(n)
                else:
                    greater.append(n)
            ret = self.quick_sort(less) + [mid] + self.quick_sort(greater)
            return ret


class TestSolution(unittest.TestCase):
    def test_quick_sort(self):
        a = [8, 5, 7, 8, 9]
        ret = Solution().quick_sort(a)
        self.assertEqual(ret, [5, 7, 8, 8, 9])


if __name__ == '__main__':
    unittest.main()
