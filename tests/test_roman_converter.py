import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    # TEST 1
    def test_num_37(self):
        self.assertEqual(decimal_to_roman(37), "XXXVII")

    # TEST 2
    def test_num_246(self):
        self.assertEqual(decimal_to_roman(246), "CCXLVI")

    # TEST 3
    def test_num_1023(self):
        self.assertEqual(decimal_to_roman(1023), "MXXIII")

    # TEST 4
    def test_num_3888(self):
        self.assertEqual(decimal_to_roman(3888), "MMMDCCCLXXXVIII")

    # TEST 5
    def test_num_74(self):
        self.assertEqual(decimal_to_roman(74), "LXXIV")

    # TEST 6
    def test_num_521(self):
        self.assertEqual(decimal_to_roman(521), "DXXI")

    # TEST 7
    def test_num_399(self):
        self.assertEqual(decimal_to_roman(399), "CCCXCIX")

    # TEST 8
    def test_num_2849(self):
        self.assertEqual(decimal_to_roman(2849), "MMDCCCXLIX")

    # TEST 9
    def test_num_58(self):
        self.assertEqual(decimal_to_roman(58), "LVIII")

    # TEST 10
    def test_num_1600(self):
        self.assertEqual(decimal_to_roman(1600), "MDC")

    # TEST 11
    def test_num_3099(self):
        self.assertEqual(decimal_to_roman(3099), "MMMXCIX")

    # TEST 12
    def test_num_1776(self):
        self.assertEqual(decimal_to_roman(1776), "MDCCLXXVI")

    # TEST 13
    def test_num_947(self):
        self.assertEqual(decimal_to_roman(947), "CMXLVII")

    # TEST 14
    def test_num_801(self):
        self.assertEqual(decimal_to_roman(801), "DCCCI")

    # TEST 15
    def test_num_70(self):
        self.assertEqual(decimal_to_roman(70), "LXX")

    # TEST 16
    def test_num_150(self):
        self.assertEqual(decimal_to_roman(150), "CL")

    # TEST 17
    def test_num_666(self):
        self.assertEqual(decimal_to_roman(666), "DCLXVI")

    # TEST 18
    def test_num_2500(self):
        self.assertEqual(decimal_to_roman(2500), "MMD")

    # TEST 19
    def test_num_1259(self):
        self.assertEqual(decimal_to_roman(1259), "MCCLIX")

    # TEST 20
    def test_num_1987(self):
        self.assertEqual(decimal_to_roman(1987), "MCMLXXXVII")

if __name__ == '__main__':
    unittest.main()
