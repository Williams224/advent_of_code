import unittest
from day_eight.day_eight import (
    determine_output_values,
    determine_segment_A,
    determine_segment_B,
    determine_segment_C,
    determine_segment_D,
    determine_segment_E,
    determine_wire_mapping,
    determine_segment_F,
    determine_segment_G,
    find_with_n_chars,
)


class TestDecoding(unittest.TestCase):
    def setUp(self) -> None:
        self.wires_list = [
            "acedgfb",
            "cdfbe",
            "gcdfa",
            "fbcad",
            "dab",
            "cefabd",
            "cdfgeb",
            "eafb",
            "cagedb",
            "ab",
        ]
        return super().setUp()

    def test_find_with_n_chars(self):
        self.assertEqual(find_with_n_chars(self.wires_list, 2), "ab")
        self.assertEqual(find_with_n_chars(self.wires_list, 3), "dab")
        self.assertEqual(find_with_n_chars(self.wires_list, 4), "eafb")
        self.assertListEqual(
            find_with_n_chars(self.wires_list, 5), ["cdfbe", "gcdfa", "fbcad"]
        )
        self.assertListEqual(
            find_with_n_chars(self.wires_list, 6), ["cefabd", "cdfgeb", "cagedb"]
        )

    def test_determine_segment_A(self):
        self.assertEqual(determine_segment_A("dab", "ab"), "d")

    def test_determine_segment_B(self):
        B = determine_segment_B(self.wires_list)
        self.assertEqual(B, "e")

    def test_determine_segment_C(self):
        C = determine_segment_C(self.wires_list)
        self.assertEqual(C, "a")

    def test_determine_segment_D(self):
        self.assertEqual(determine_segment_D(self.wires_list), "f")

    def test_determine_segment_E(self):
        self.assertEqual(determine_segment_E(self.wires_list), "g")

    def test_determine_segment_F(self):
        F = determine_segment_F(self.wires_list)
        self.assertEqual(F, "b")

    def test_determine_segment_G(self):
        G = determine_segment_G(self.wires_list)
        self.assertEqual(G, "c")

    def test_determine_display_mapping(self):
        determine_wire_mapping(self.wires_list)

    def test_determine_output_values(self):
        values_list = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]
        expected_output = 5353
        actual_output = determine_output_values(
            values_list, determine_wire_mapping(self.wires_list)
        )
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
