import unittest
import numpy as np
from .day_eight import (
    check_less_than,
    load_data,
    count_visible,
    calc_external_visible,
    calc_scenic_scores,
)


class testDayEight(unittest.TestCase):
    def setUp(self) -> None:
        self.map = load_data(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_eight/test_input.txt"
        )
        return super().setUp()

    def test_check_less_than(self):
        map = self.map
        # check
        self.assertEqual(check_less_than(1, 1, map[1, 1], map, "initial")[0], True)
        self.assertEqual(check_less_than(1, 2, map[1, 2], map, "initial")[0], True)
        self.assertEqual(check_less_than(2, 1, map[1, 2], map, "initial")[0], True)
        self.assertEqual(check_less_than(1, 3, map[1, 3], map, "initial")[0], False)
        self.assertEqual(check_less_than(2, 2, map[2, 2], map, "initial")[0], False)
        self.assertEqual(check_less_than(2, 3, map[2, 3], map, "initial")[0], True)
        self.assertEqual(check_less_than(4, 1, map[4, 1], map, "initial")[0], True)
        self.assertEqual(check_less_than(3, 3, map[3, 3], map, "initial")[0], False)

    def test_count_visible(self):
        self.assertEqual(count_visible(self.map), 5)

    def test_external_visible(self):
        self.assertEqual(calc_external_visible(self.map), 16)

    def test_vis_dists(self):
        visible, distances = check_less_than(
            1,
            2,
            self.map[1, 2],
            self.map,
            "initial",
        )
        self.assertTupleEqual(distances, (1, 2, 1, 2))
        visible, distances = check_less_than(
            3,
            2,
            self.map[3, 2],
            self.map,
            "initial",
        )
        self.assertTupleEqual(distances, (2, 2, 2, 1))

    def test_scenic_scores(self):

        scenic_scores = calc_scenic_scores(self.map)

        print("hello")
