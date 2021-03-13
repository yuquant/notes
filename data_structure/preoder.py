# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
中序遍历可以输出二叉树的按从小到大排序的数组
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self._ret = []

    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        # 访问节点数值,放到前边就是前序遍历，后边就是后序遍历
        val = root.val
        self._ret.append(val)

        for child in root.children:
            self.preorder(child)
            # self._ret.extend(self.preorder(child))  错误写法，不需要，否则错误
        return self._ret
