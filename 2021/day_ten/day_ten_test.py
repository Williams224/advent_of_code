import unittest

from day_ten.day_ten import find_closing_chars, is_line_corrupt


class TestDayTen(unittest.TestCase):
    def setUp(self) -> None:
        with open("day_ten/test_input.txt") as f:
            tmp_lines = f.readlines()
        self.lines = [l.strip("\n") for l in tmp_lines]

        return super().setUp()

    def test_is_line_corrupt(self):
        self.assertEqual(is_line_corrupt(self.lines[0]), (False, None))
        self.assertEqual(is_line_corrupt(self.lines[1]), (False, None))
        self.assertEqual(is_line_corrupt(self.lines[2]), (True, "}"))
        self.assertEqual(is_line_corrupt(self.lines[3]), (False, None))
        self.assertEqual(is_line_corrupt(self.lines[4]), (True, ")"))
        self.assertEqual(is_line_corrupt(self.lines[5]), (True, "]"))
        self.assertEqual(is_line_corrupt(self.lines[6]), (False, None))
        self.assertEqual(is_line_corrupt(self.lines[7]), (True, ")"))
        self.assertEqual(is_line_corrupt(self.lines[8]), (True, ">"))
        self.assertEqual(is_line_corrupt(self.lines[0]), (False, None))

    def test_find_closing_chars(self):
        closing_chars = find_closing_chars("[({(<(())[]>[[{[]{<()<>>")
        print(closing_chars)
