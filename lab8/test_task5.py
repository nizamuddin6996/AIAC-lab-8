import unittest
from task5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-12-31"), "31-12-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-11-09"), "09-11-1999")
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")
        self.assertEqual(convert_date_format(" 2021-07-15 "), "15-07-2021")  # trims spaces

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/12/31")
        with self.assertRaises(ValueError):
            convert_date_format("31-12-2023")
        with self.assertRaises(ValueError):
            convert_date_format("2023-12")
        with self.assertRaises(ValueError):
            convert_date_format("2023-12-31-01")
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_non_numeric(self):
        with self.assertRaises(ValueError):
            convert_date_format("abcd-ef-gh")
        with self.assertRaises(ValueError):
            convert_date_format("year-month-day")

    def test_leading_zeros(self):
        self.assertEqual(convert_date_format("2023-04-05"), "05-04-2023")
        self.assertEqual(convert_date_format("2023-12-01"), "01-12-2023")

if __name__ == "__main__":
    unittest.main()