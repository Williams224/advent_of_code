import unittest
from .day_twenty import get_new_index, move_element


class TestDayTwenty(unittest.TestCase):
    def test_get_new_index(self):
        self.assertEqual(get_new_index(0, -6258, 5000), 3740)
        self.assertEqual(get_new_index(0, 1, 7), 1)
        self.assertEqual(get_new_index(0, 2, 7), 2)
        self.assertEqual(get_new_index(1, -3, 7), 4)
        self.assertEqual(get_new_index(2, 3, 7), 5)
        self.assertEqual(get_new_index(2, -2, 7), 6)
        self.assertEqual(get_new_index(3, 0, 7), 3)
        self.assertEqual(get_new_index(5, 4, 7), 3)
        self.assertEqual(get_new_index(2, -17, 7), 5)
        self.assertEqual(get_new_index(0, -4, 7), 2)
        self.assertEqual(get_new_index(0, 10, 7), 4)

    def test_move(self):
        orig_list = [1, 2, -3, 3, -2, 0, 4]
        new_list = orig_list.copy()
        expected = [2, 1, -3, 3, -2, 0, 4]
        actual = move_element(orig_list, 0, new_list)
        self.assertListEqual(expected, actual)

        expected = [1, -3, 2, 3, -2, 0, 4]
        actual = move_element(orig_list, 1, new_list)
        self.assertListEqual(expected, actual)

        expected = [1, 2, 3, -2, -3, 0, 4]
        actual = move_element(orig_list, 2, new_list)
        self.assertListEqual(expected, actual)

        expected = [1, 2, -2, -3, 0, 3, 4]
        actual = move_element(orig_list, 3, new_list)
        self.assertListEqual(expected, actual)

        expected = [1, 2, -3, 0, 3, 4, -2]
        actual = move_element(orig_list, 4, new_list)
        self.assertListEqual(expected, actual)

        expected = [1, 2, -3, 0, 3, 4, -2]
        actual = move_element(orig_list, 5, new_list)
        self.assertListEqual(expected, actual)

        expected = [1, 2, -3, 4, 0, 3, -2]
        actual = move_element(orig_list, 6, new_list)
        self.assertListEqual(expected, actual)

        new_list = [-4, 2, -3, 3, -2, 0, 4]
        orig_list = [-4, 2, -3, 3, -2, 0, 4]
        expected = [2, -3, -4, 3, -2, 0, 4]
        actual = move_element(orig_list, 0, new_list)
        self.assertListEqual(expected, actual)

        new_list = [10, 2, -3, 3, -2, 0, 4]
        orig_list = [10, 2, -3, 3, -2, 0, 4]
        expected = [2, -3, 3, -2, 10, 0, 4]
        actual = move_element(orig_list, 0, new_list)
        self.assertListEqual(expected, actual)

        new_list = [6, 2, -3, 3, -2, 0, 4]
        orig_list = [6, 2, -3, 3, -2, 0, 4]
        expected = [2, -3, 3, -2, 0, 4, 6]
        actual = move_element(orig_list, 0, new_list)
        self.assertListEqual(expected, actual)
