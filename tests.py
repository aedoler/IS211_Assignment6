#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import unittest
import conversions


class testCelsiusToKelvin(unittest.TestCase):
    knownValues = [(0, 273.15), (50, 323.15), (100, 373.15), (555, 828.15)]
    """convertCelsiusToKelvin should return the correct value"""
    def testCorrectResult(self):
        for cel, kel in self.knownValues:
            result = conversions.convertCelsiusToKelvin(cel)
            self.assertEqual(kel, result)


class testCelsiusToFarenheit(unittest.TestCase):
    knownValues = [(0, 32.0), (16, 60.8), (27, 80.6), (17, 62.6)]
    """convertCelsiusToFarenheit should return the correct value"""
    def testCorrectResult(self):
        for cel, far in self.knownValues:
            result = conversions.convertCelsiusToFarenheit(cel)
            self.assertEqual(far, result)


class testFarenheihtToCelsius(unittest.TestCase):
    knownValues = [(32, 0), (64, 17), (80, 26), (88, 31)]
    """convertCelsiusToFarenheit should return the correct value"""
    def testCorrectResult(self):
        for far, cel in self.knownValues:
            result = conversions.convertFarenheitToCelsius(far)
            self.assertEqual(cel, result)

class testFarenheihtToKelvin(unittest.TestCase):
    knownValues = [(3, 256.15), (5, 258.15), (100, 310.15), (4444, 2724.15)]
    """convertCelsiusToFarenheit should return the correct value"""
    def testCorrectResult(self):
        for far, kel in self.knownValues:
            result = conversions.convertFarenheitToKelvin(far)
            self.assertEqual(kel, result)


class testKelvinToCelsius(unittest.TestCase):
    knownValues = [(402, 128.85000000000002), (350, 76.85000000000002), (1000, 726.85), (800, 526.85)]
    """convertCelsiusToFarenheit should return the correct value"""
    def testCorrectResult(self):
        for kel, cel in self.knownValues:
            result = conversions.convertKelvinToCelsius(kel)
            self.assertEqual(cel, result)

class testKelvinToFarenheit(unittest.TestCase):
    knownValues = [(300, 80.33000000000004), (270, 26.33000000000004),
                   (455, 359.33000000000004), (600, 620.33)]
    """convertCelsiusToFarenheit should return the correct value"""
    def testCorrectResult(self):
        for kel, far in self.knownValues:
            result = conversions.convertKelvinToFarenheit(kel)
            self.assertEqual(far, result)




if __name__ == "__main__":
    unittest.main()