# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""
from typing import List
import unittest

#
# class Solution:
#     """
#     错误解法，死循环
#     """
#     def findDuplicate(self, nums: List[int]) -> int:
#         length = len(nums)
#         slow = 0
#         fast = 0
#         while True:
#             if slow != fast and nums[slow] == nums[fast]:
#                 return nums[slow]
#             slow += 1
#             fast += 2
#             slow %= length
#             fast %= length


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/is-subsequence/solution/pan-duan-zi-xu-lie-by-leetcode-solution/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :param s:
        :param t:
        :return:
        """
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n



if __name__ == '__main__':
    unittest.main()
