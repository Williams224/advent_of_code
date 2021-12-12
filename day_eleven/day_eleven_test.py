import numpy as np
import unittest

from day_eleven.day_eleven import check_and_flash, load_map


class TestDayEleven(unittest.TestCase):
    def setUp(self) -> None:
        self.map = load_map("day_eleven/test_input.txt") + 2
        self.step_flash_indices = []
        return super().setUp()

    def test_check_and_flash(self):
        check_and_flash(0, 2, self.map, self.step_flash_indices)
        print(map)
