import unittest
from .day_four import read_input, check_full_overlap, check_any_overlap

"""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


class TestDayFourInputRead(unittest.TestCase):
    def test_day_four_read_input(self):

        sections = read_input(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_four/test_input.txt"
        )

        self.assertTupleEqual(sections[0], ((2, 4), (6, 8)))

        self.assertTupleEqual(sections[1], ((2, 3), (4, 5)))

        self.assertTupleEqual(sections[2], ((5, 7), (7, 9)))


class TestDayFour(unittest.TestCase):
    def setUp(self) -> None:
        self.sections = read_input(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_four/test_input.txt"
        )
        return super().setUp()

    def test_check_overlap(self):
        self.assertEqual(check_full_overlap(self.sections[0]), False)
        self.assertEqual(check_full_overlap(self.sections[1]), False)
        self.assertEqual(check_full_overlap(self.sections[2]), False)
        self.assertEqual(check_full_overlap(self.sections[3]), True)
        self.assertEqual(check_full_overlap(self.sections[4]), True)
        self.assertEqual(check_full_overlap(self.sections[5]), False)

    def test_check_any_overlap(self):
        self.assertEqual(check_any_overlap(self.sections[0]), False)
        self.assertEqual(check_any_overlap(self.sections[1]), False)
        self.assertEqual(check_any_overlap(self.sections[2]), True)
        self.assertEqual(check_any_overlap(self.sections[3]), True)
        self.assertEqual(check_any_overlap(self.sections[4]), True)
        self.assertEqual(check_any_overlap(self.sections[5]), True)
