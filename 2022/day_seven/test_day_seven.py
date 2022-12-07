import unittest
from .day_seven import read_commands, fill_dir_sizes, sum_all_limit
import numpy as np


class testInput(unittest.TestCase):
    def test_read_input(self):
        parent_node = read_commands(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_seven/test_input.txt"
        )
        fill_dir_sizes(parent_node)
        sizes = []
        sum_all_limit(parent_node, 100000, sizes)
        self.assertListEqual(sizes, [94853, 584])
        self.assertEqual(np.sum(sizes), 95437)
