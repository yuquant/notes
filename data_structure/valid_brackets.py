# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
"""

import unittest


class Stack:
    def __init__(self):
        self._stack = []

    def is_empty(self) -> bool:
        return not bool(self._stack)

    def pull(self):
        return self._stack.pop()

    def push(self, element):
        self._stack.append(element)

    def top(self):
        return self._stack[-1]


class Solution:
    def is_valid(self, code: str) -> bool:
        cleaned_code = self._get_brackets(code)
        ret = self._is_brackets_valid(cleaned_code)
        return ret

    def _is_brackets_valid(self, brackets: str):
        if not brackets:
            return True
        stack = Stack()
        bracket_dict = {'{': '}', '(': ')', '[': ']'}
        for s in brackets:
            if s in bracket_dict:
                stack.push(s)
            else:
                if stack.is_empty():
                    return False
                if s != bracket_dict[stack.pull()]:
                    return False
        ret = stack.is_empty()
        return ret

    def _get_brackets(self, code: str):
        brackets = set(['{', '}', '[', ']', '(', ')'])
        ret = []
        for s in code:
            if s in brackets:
                ret.append(s)
        return ''.join(ret)


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
