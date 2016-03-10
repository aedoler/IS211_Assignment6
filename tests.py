#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import unittest
import conversions


class testCelciusToKelvin(unittest.TestCase):
    knownValues = [(0, 273.15), (50, 323.15), (100, 373.15), (555, 828.15)]
    """convertCelciusToKelvin should return the correct value"""
    def testCorrectResult(self):
        for cel, kel in self.knownValues:
            result = conversions.convertCelsiusToKelvin(cel)
            self.assertEqual(kel, result)






if __name__ == "__main__":
    unittest.main()