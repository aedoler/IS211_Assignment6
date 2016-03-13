#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import unittest
import conversions
import conversions_refactored



class testCelsiusToKelvin(unittest.TestCase):
    """convertCelsiusToKelvin should return the correct value"""
    knownValues = [(0, 273.15), (50, 323.15), (100, 373.15), (555, 828.15)]
    def testCorrectResult(self):
        for cel, kel in self.knownValues:
            result = conversions.convertCelsiusToKelvin(cel)
            self.assertEqual(kel, result)


class testCelsiusToFarenheit(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(0, 32.0), (16, 60.8), (27, 80.6), (17, 62.6)]
    def testCorrectResult(self):
        for cel, far in self.knownValues:
            result = conversions.convertCelsiusToFarenheit(cel)
            self.assertEqual(far, result)


class testFarenheihtToCelsius(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(32, 0), (64, 17), (80, 26), (88, 31)]
    def testCorrectResult(self):
        for far, cel in self.knownValues:
            result = conversions.convertFarenheitToCelsius(far)
            self.assertEqual(cel, result)

class testFarenheihtToKelvin(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(3, 256.15), (5, 258.15), (100, 310.15), (4444, 2724.15)]
    def testCorrectResult(self):
        for far, kel in self.knownValues:
            result = conversions.convertFarenheitToKelvin(far)
            self.assertEqual(kel, result)


class testKelvinToCelsius(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(402, 128.85000000000002), (350, 76.85000000000002), (1000, 726.85), (800, 526.85)]
    def testCorrectResult(self):
        for kel, cel in self.knownValues:
            result = conversions.convertKelvinToCelsius(kel)
            self.assertEqual(cel, result)

class testKelvinToFarenheit(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(300, 80.33000000000004), (270, 26.33000000000004),
                   (455, 359.33000000000004), (600, 620.33)]
    def testCorrectResult(self):
        for kel, far in self.knownValues:
            result = conversions.convertKelvinToFarenheit(kel)
            self.assertEqual(far, result)


class testCelsiusToKelvin2(unittest.TestCase):
    """Tests that each conversions is working properly and that an
    error is thrown when necessary"""
    knownValues = [(0, 273.15), (50, 323.15), (100, 373.15), (555, 828.15)]
    def testCelsiusToKelvin(self):
        """convertCelsiusToKelvin should return the correct value"""
        for cel, kel in self.knownValues:
            result = conversions_refactored.allConversions('celsius', 'kelvin', cel)
            self.assertEqual(kel, result)

class testCelsiusToFarenheit2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(0, 32.0), (16, 60.8), (27, 80.6), (17, 62.6)]
    def testCorrectResult(self):
        for cel, far in self.knownValues:
            result = conversions_refactored.allConversions('celsius', 'farenheit', cel)
            self.assertEqual(far, result)

class testFarenheihtToCelsius2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(32, 0), (64, 17.77777777777778), (80, 26.666666666666668), (88, 31.11111111111111)]
    def testCorrectResult(self):
        for far, cel in self.knownValues:
            result = conversions_refactored.allConversions('farenheit', 'celsius', far)
            self.assertEqual(cel, result)

class testFarenheihtToKelvin2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(3, 257.0388888888889), (5, 258.15), (100, 310.92777777777775), (4444, 2724.2611111111114)]
    def testCorrectResult(self):
        for far, kel in self.knownValues:
            result = conversions_refactored.allConversions('farenheit', 'kelvin', far)
            self.assertEqual(kel, result)

class testKelvinToCelsius2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(402, 128.85000000000002), (350, 76.85000000000002), (1000, 726.85), (800, 526.85)]
    def testCorrectResult(self):
        for kel, cel in self.knownValues:
            result = conversions_refactored.allConversions('kelvin', 'celsius', kel)
            self.assertEqual(cel, result)

class testKelvinToFarenheit2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(300, 80.33000000000004), (270, 26.33000000000004),
                   (455, 359.33000000000004), (600, 620.33)]
    def testCorrectResult(self):
        for kel, far in self.knownValues:
            result = conversions_refactored.allConversions('kelvin', 'farenheit', kel)
            self.assertEqual(far, result)

class testMilesToYards(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(4,  7040.0), (6, 10560.0),
                   (40, 70400.0), (200, 352000.0)]
    def testCorrectResult(self):
        for mile, yard in self.knownValues:
            result = conversions_refactored.allConversions('miles', 'yards', mile)
            self.assertEqual(yard, result)

class testMilesToYards(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(1,  1609.3470878864446), (6, 9656.082527318667),
                   (50, 80467.35439432222), (500, 804673.5439432223)]
    def testCorrectResult(self):
        for mile, meter in self.knownValues:
            result = conversions_refactored.allConversions('miles', 'meters', mile)
            self.assertEqual(meter, result)

class TestConversion(unittest.TestCase):
    bc = [('celsius', 'miles'), ('celsius', 'yards'), ('celsius', 'meters'),
          ('farenheit', 'miles'), ('farenheit', 'yards'), ('farenheit', 'miles'),
          ('kelvin', 'miles'), ('kelvin', 'yards'), ('kelvin', 'miles')]
    def testConversionNotPossible(self):
        for input in self.bc:
            self.assertRaises(conversions_refactored.ConversionNotPossible,
                              conversions_refactored.allConversions, input[0], input[1], -1)
    def testConversionNotPossible2(self):
        for input in self.bc:
            self.assertRaises(conversions_refactored.ConversionNotPossible,
                              conversions_refactored.allConversions, input[1], input[0], -1)


if __name__ == "__main__":
    unittest.main()

