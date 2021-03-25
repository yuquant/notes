# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""
import unittest
import numpy as np


class Conv:
    def run(self, image_arr, kernel):
        res = np.zeros_like(image_arr)
        kernel_size = kernel.shape[0]
        width, height = image_arr.shape
        padding = int(kernel_size / 2)
        for i in range(padding, width - padding):
            for j in range(padding, height - padding):
                res[i, j] = np.sum(image_arr[i - padding:i + padding + 1, j - padding:j + padding + 1] * kernel)

        return res


class TestConv(unittest.TestCase):
    def test_run(self):
        image_arr = np.ones((10, 15))
        kernel = np.ones((3, 3))
        conv = Conv()
        res = conv.run(image_arr, kernel)
        self.assertEqual(res.shape, image_arr.shape)


if __name__ == '__main__':
    unittest.main()
