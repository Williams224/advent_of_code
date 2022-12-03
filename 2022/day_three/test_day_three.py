import unittest
from .day_three import line_priority_score, get_group, get_group_priority_score
import numpy as np


class TestScoreLine(unittest.TestCase):
    def setUp(self) -> None:
        self.test_lines = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        return super().setUp()

    def test_line_priority_score(self):
        self.assertEqual(line_priority_score(self.test_lines[0]), 16)
        self.assertEqual(line_priority_score(self.test_lines[1]), 38)
        self.assertEqual(line_priority_score(self.test_lines[2]), 42)
        self.assertEqual(line_priority_score(self.test_lines[3]), 22)
        self.assertEqual(line_priority_score(self.test_lines[4]), 20)
        self.assertEqual(line_priority_score(self.test_lines[5]), 19)

    def test_group_priority_score(self):
        gr_prio_scores = []
        for gr in get_group(self.test_lines, 3):
            gr_prio_scores.append(get_group_priority_score(gr))

        self.assertListEqual(gr_prio_scores, [18, 52])
        self.assertEqual(np.sum(gr_prio_scores), 70)
