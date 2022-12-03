import unittest

from day_sixteen.day_sixteen import hex_to_bin, split_binary


class TestDaySixteen(unittest.TestCase):
    def setUp(self) -> None:
        self.test_input_one = hex_to_bin("8A004A801A8002F478")
        self.test_input_two = hex_to_bin("620080001611562C8802118E34")
        self.test_input_three = hex_to_bin("C0015000016115A2E0802F182340")
        self.test_input_four = hex_to_bin("A0016C880162017C3686B18A3D4780")
        return super().setUp()

    def test_strings_to_bin(self):
        first_list, end_pos = split_binary(0, self.test_input_one)
        self.assertEqual(end_pos, len(self.test_input_one) - 1)