# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :


"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head):
        pre = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre
