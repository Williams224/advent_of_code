import unittest
from .day_six import find_first_marker


class TestDaySix(unittest.TestCase):
    def test_find_first_marker(self):
        self.assertEqual(find_first_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
        self.assertEqual(find_first_marker("nppdvjthqldpwncqszvftbrmjlhg", 4), 6)
        self.assertEqual(find_first_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)
        self.assertEqual(find_first_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4), 11)
        self.assertEqual(find_first_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
        self.assertEqual(find_first_marker("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(find_first_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
        self.assertEqual(find_first_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)
