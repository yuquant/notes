# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
"""

import unittest


class Solution:
    def is_valid(self, brackets: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for s in brackets:
            if s in pairs:
                stack.append(s)
            else:
                if stack:
                    left_bracket = stack.pop()
                    if pairs[left_bracket] != s:
                        return False
                else:
                    return False
        return not bool(stack)


class TestSolution(unittest.TestCase):
    def test_is_valid(self):
        s = Solution()
        self.assertTrue(s.is_valid('{}()[]'))
        self.assertTrue(s.is_valid('{()[]}'))
        self.assertFalse(s.is_valid('}()[]{'))
        self.assertFalse(s.is_valid('{(()[]'))
        self.assertFalse(s.is_valid('('))


if __name__ == '__main__':
    unittest.main()
