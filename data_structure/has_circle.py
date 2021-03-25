# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""

# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""

import unittest


class ListNode:
    def __init__(self):
        self.next = None


class Solution:
    def has_circle(self, node: ListNode) -> bool:
        if not node.next:
            return False
        slow = node
        fast = node.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True


class TestSolution(unittest.TestCase):
    def test_has_circle(self):
        pass
