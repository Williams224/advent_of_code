import unittest
from .day_twenty_five import SNAFU_to_decimal, decimal_to_SNAFU


class testSNAFU(unittest.TestCase):
    def test_snafu_to_decimal(self):
        self.assertEqual(SNAFU_to_decimal("1=-0-2"), 1747)
        self.assertEqual(SNAFU_to_decimal("12111"), 906)
        self.assertEqual(SNAFU_to_decimal("2=0="), 198)
        self.assertEqual(SNAFU_to_decimal("21"), 11)
        self.assertEqual(SNAFU_to_decimal("2=01"), 201)
        self.assertEqual(SNAFU_to_decimal("111"), 31)
        self.assertEqual(SNAFU_to_decimal("20012"), 1257)
        self.assertEqual(SNAFU_to_decimal("112"), 32)
        self.assertEqual(SNAFU_to_decimal("1=-1="), 353)
        self.assertEqual(SNAFU_to_decimal("1-12"), 107)
        self.assertEqual(SNAFU_to_decimal("12"), 7)
        self.assertEqual(SNAFU_to_decimal("1="), 3)
        self.assertEqual(SNAFU_to_decimal("122"), 37)

    def test_decimal_to_snafu(self):
        self.assertEqual(decimal_to_SNAFU(198), "2=0=")
        self.assertEqual(decimal_to_SNAFU(1747), "1=-0-2")
        self.assertEqual(decimal_to_SNAFU(906), "12111")
        self.assertEqual(decimal_to_SNAFU(201), "2=01")
        self.assertEqual(decimal_to_SNAFU(353), "1=-1=")
        self.assertEqual(decimal_to_SNAFU(3), "1=")
