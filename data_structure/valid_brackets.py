# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
"""

import unittest


class Solution:
    def is_valid(self, code: str) -> bool:
        cleaned_code = self._get_brackets(code)
        ret = self._is_brackets_valid(cleaned_code)
        return ret

    def _is_brackets_valid(self, brackets: str):
        if not brackets:
            return True
        stack = []
        bracket_dict = {'{': '}', '(': ')', '[': ']'}
        for s in brackets:
            if s in bracket_dict:
                stack.append(s)
            else:
                if len(stack) == 0:
                    return False
                if s != bracket_dict[stack.pop()]:
                    return False
        ret = not stack
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
