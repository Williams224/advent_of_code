import unittest
import numpy as np

from day_nine.day_nine import find_basin_value


class TestDayNine(unittest.TestCase):
    def setUp(self) -> None:
        with open("day_nine/test_input.txt", "r") as f:
            lines = f.readlines()
        lines_lists = []
        for l in lines:
            lines_lists.append(list(l.strip("\n")))

        self.map = np.array(lines_lists, dtype=int)
        self.identities = np.zeros((5, 10)) - 1
        return super().setUp()

    def test_find_basin_value(self):
        coords_same_basin = []
        coords_same_basin = find_basin_value(1, 0, self.map, "left", coords_same_basin)
        self.assertListEqual([(0, 0)], coords_same_basin)
        coords_same_basin_down = []
        coords_same_basin_down = find_basin_value(
            9, 0, self.map, "down", coords_same_basin_down
        )
        self.assertListEqual([(9, 1), (9, 2)], coords_same_basin_down)
        print(coords_same_basin)