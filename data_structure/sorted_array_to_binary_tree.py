# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums:
            return
        else:
            mid_index = len(nums) // 2
            root = TreeNode(nums[mid_index])
            nums_left = nums[:mid_index]
            nums_right = nums[mid_index + 1:]  # 注意这里要跳过一个
            root.left = self.sortedArrayToBST(nums_left)
            root.right = self.sortedArrayToBST(nums_right)
        return root
