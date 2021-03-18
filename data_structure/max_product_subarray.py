# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
152
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(len(nums))] for _ in range(2)]  # 注意此处初始化为0，不过1似乎也可以通过
        for i, num in enumerate(nums):
            if i == 0:
                dp[0][0] = nums[0]
            else:
                dp[0][i] = max(dp[0][i - 1] * num, dp[1][i - 1] * num, num)
                dp[1][i] = min(dp[0][i - 1] * num, dp[1][i - 1] * num, num)
        return max(dp[0])
        # 注意由于0的存在性，会导致分割
