import unittest
from pesel import main

class TestValidate(unittest.TestCase):

    def test_date_getter(self):
        result = main.date_getter('99030398126')
        self.assertEqual(result,(1999, 3, 3))

    def test_gender_getter(self):
        result = main.gender_getter('99030398126')
        self.assertEqual(result,'women')

    def test_validator(self):
        with self.assertRaises(ValueError):
            main.date_getter('')
            main.gender_getter('')
            main.date_getter('1111111111111111111111111111111111111111111')

