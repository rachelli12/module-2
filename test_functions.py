"""
Program name: test_functions.py
Author: Rachel Li
Last date modified: 06/02/2020

Purpose of this program is to test function.
"""
import unittest
from main import camper_age_input as cai


class FunctionTestCase(unittest.TestCase):
    def test_4_years_to_months(self):
        #4 years old should be 48 months
        self.assertEqual(48, cai.convert_to_months(4))

if __name__=='__main__':
    unittest.main()

