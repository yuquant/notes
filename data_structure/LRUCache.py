# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
https://leetcode-cn.com/problems/lru-cache/submissions/
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()
        self._size = 0

    def get(self, key: int) -> int:
        if key in self._cache:
            self._move_exist_key_up(key)
            return self._cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:  # in
            self._update_exist_key(key, value)  # 注意这里容易出错
        elif self._size == self._capacity:  # full
            self._cache.popitem(last=False)
            self._cache[key] = value
        else:  # not full and not in
            self._cache[key] = value
            self._size += 1

    def _move_exist_key_up(self, key):
        if key in self._cache:
            self._cache[key] = self._cache.pop(key)
        else:
            raise KeyError

    def _update_exist_key(self, key, value):
        if key in self._cache:
            self._cache.pop(key)
            self._cache[key] = value
        else:
            raise KeyError
