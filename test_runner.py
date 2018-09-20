#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import quasi_sort

class TestQuasiSort(unittest.TestCase):

  def test_offsets(self):
    test_arrs = [
      [0, 3, -3, 1, 0, -1],
      [0, 0, -1, 3, 1, -3],
      [-1, -3, 0, 3, 0, 1]
    ]
    test_arr_long = [-4, 13, 10, -13, 0, 0, -13, 3, 7, 17, -16, -4, -8, 9, 2, 0, -9, -2, -12, -17, -19, -19]
    for arr in test_arrs:
      self.assertEqual((2, 4), quasi_sort.find_offset(arr))
    self.assertEqual((12, 15), quasi_sort.find_offset(test_arr_long))

  def test_arrange(self):
    arrs = [
      [-1, 3, -3, 0, 1, 0],
      [0, -1, -3, 0, 1, 3],
      [1, -1, 3, 0, -3, 0],
      [-1, 0, 1, -3, 3, 0],
      [0, 3, -3, 1, 0, -1],
      [0, 0, -1, 3, 1, -3],
      [-1, -3, 0, 3, 0, 1],
      [1, -1, -3, 0, 0, 3],
      [1, -3, -1, 3, 0, 0],
      [0, 1, -1, 3, 0, -3],
      [-4, 13, 10, 0, -13, -13, 3, 7, 17, -16, -4, -8, 9, 2, 0, -9, -2, 0, -12, -17, -19, -19],
      [0, -19, -13, 17, 2, -9, -4, 9, 0, 13, -4, 3, -19, -16, -17, 7, -12, 10, -8, -2, 0, -13],
      [-9, 0, 17, 3, 10, 13, 2, 7, -13, -4, -16, -17, -8, -13, -19, -12, 9, 0, -19, 0, -2, -4]
      ]
    for arr in arrs:
      quasi_sorted = quasi_sort.arrange(arr)
      offsetZer, offsetPos = quasi_sort.find_offset(arr)
      for elem in quasi_sorted[ : offsetZer]:
        self.assertLess(elem, 0)
      for elem in quasi_sorted[offsetZer : offsetPos]:
        self.assertEqual(elem, 0)
      for elem in quasi_sorted[offsetPos : ]:
        self.assertGreater(elem, 0)


if __name__ == '__main__':
    unittest.main()