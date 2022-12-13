import unittest
from .day_thriteen import check_list, read_input, bubble_sort
import numpy as np


class testDayThirteen(unittest.TestCase):
    def test_check_list(self):

        self.assertTrue(check_list([[2]], [[6]], 0))
        self.assertTrue(check_list([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], 0))
        self.assertTrue(check_list([[1], [2, 3, 4]], [[1], 4], 0))
        self.assertFalse(check_list([9], [[8, 7, 6]], 0))
        self.assertTrue(check_list([[4, 4], 4, 4], [[4, 4], 4, 4, 4], 0))
        self.assertFalse(check_list([7, 7, 7, 7], [7, 7, 7], 0))
        self.assertTrue(check_list([], [3], 0))
        self.assertFalse(check_list([[[]]], [[]], 0))
        self.assertFalse(
            check_list(
                [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
                0,
            )
        )

    def test_all(self):
        pairs = read_input(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_thirteen/test_input.txt"
        )
        outcomes = []
        for pair in pairs:
            outcomes.append(check_list(pair[0], pair[1], 0))

        indices_sum = np.sum((np.where(np.array(outcomes))[0] + 1))

        self.assertEqual(indices_sum, 13)

    def test_bubble_sort(self):

        l = [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]]
        l_sorted = bubble_sort(l)
        l_wrong = [[1, 1, 5, 1, 1], [1, 1, 3, 1, 1]]
        l_sorted_wrong = bubble_sort(l_wrong)

        self.assertListEqual(l_sorted, [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]])
        self.assertListEqual(l_sorted_wrong, [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]])

        l_markers = [[[6], 5], [[2]]]

        l_markers_sorted = bubble_sort(l_markers)

        print(l_markers_sorted)
