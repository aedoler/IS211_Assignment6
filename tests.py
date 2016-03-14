#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import unittest
import conversions
import conversions_refactored



class testCelsiusToKelvin(unittest.TestCase):
    """convertCelsiusToKelvin should return the correct value"""
    knownValues = [(0, 273.0), (50, 323.0), (100, 373.0), (555, 828.0)]
    def testCorrectResult(self):
        for cel, kel in self.knownValues:
            result = conversions.convertCelsiusToKelvin(cel)
            self.assertEqual(kel, result)


class testCelsiusToFarenheit(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(0, 32.0), (16, 61.0), (27, 81.0), (17, 63.0)]
    def testCorrectResult(self):
        for cel, far in self.knownValues:
            result = conversions.convertCelsiusToFarenheit(cel)
            self.assertEqual(far, result)


class testFarenheihtToCelsius(unittest.TestCase):
    """convertFarenheitToCelsius should return the correct value"""
    knownValues = [(32, 0), (64, 17), (80, 26), (88, 31)]
    def testCorrectResult(self):
        for far, cel in self.knownValues:
            result = conversions.convertFarenheitToCelsius(far)
            self.assertEqual(cel, result)

class testFarenheihtToKelvin(unittest.TestCase):
    """convertFarenheitToKelvin should return the correct value"""
    knownValues = [(3, 256.0), (5, 258.0), (100, 310.0), (4444, 2724.0)]
    def testCorrectResult(self):
        for far, kel in self.knownValues:
            result = conversions.convertFarenheitToKelvin(far)
            self.assertEqual(kel, result)


class testKelvinToCelsius(unittest.TestCase):
    """convertKelvinToFarenheit should return the correct value"""
    knownValues = [(402, 129.0), (350, 77.0), (1000, 727.0), (800, 527.0)]
    def testCorrectResult(self):
        for kel, cel in self.knownValues:
            result = conversions.convertKelvinToCelsius(kel)
            self.assertEqual(cel, result)

class testKelvinToFarenheit(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(300, 81.0), (270, 27.0),
                   (455, 360.0), (600, 621.0)]
    def testCorrectResult(self):
        for kel, far in self.knownValues:
            result = conversions.convertKelvinToFarenheit(kel)
            self.assertEqual(far, result)


class testCelsiusToKelvin2(unittest.TestCase):
    """Tests that each conversions is working properly and that an
    error is thrown when necessary"""
    knownValues = [(0, 273.0), (50, 323.0), (100, 373.0), (555, 828.0)]
    def testCelsiusToKelvin(self):
        """convertCelsiusToKelvin should return the correct value"""
        for cel, kel in self.knownValues:
            result = conversions_refactored.allConversions('celsius', 'kelvin', cel)
            self.assertEqual(kel, result)

class testCelsiusToFarenheit2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(0, 32.0), (16, 61.0), (27, 81.0), (17, 63.0)]
    def testCorrectResult(self):
        for cel, far in self.knownValues:
            result = conversions_refactored.allConversions('celsius', 'farenheit', cel)
            self.assertEqual(far, result)

class testFarenheihtToCelsius2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(32, 0), (64, 18.0), (80, 27.0), (88, 31.0)]
    def testCorrectResult(self):
        for far, cel in self.knownValues:
            result = conversions_refactored.allConversions('farenheit', 'celsius', far)
            self.assertEqual(cel, result)

class testFarenheihtToKelvin2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(3, 257.0), (5, 258.0), (100, 311.0), (4444, 2724.0)]
    def testCorrectResult(self):
        for far, kel in self.knownValues:
            result = conversions_refactored.allConversions('farenheit', 'kelvin', far)
            self.assertEqual(kel, result)

class testKelvinToCelsius2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(402, 129.0), (350, 77.0), (1000, 727.0), (800, 527.0)]
    def testCorrectResult(self):
        for kel, cel in self.knownValues:
            result = conversions_refactored.allConversions('kelvin', 'celsius', kel)
            self.assertEqual(cel, result)

class testKelvinToFarenheit2(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(300, 80.0), (270, 26.0),
                   (455, 359.0), (600, 620.0)]
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

class testMilesToMeters(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(1,  1609.0), (6, 9656.0),
                   (50, 80467.0), (500, 804674.0)]
    def testCorrectResult(self):
        for mile, meter in self.knownValues:
            result = conversions_refactored.allConversions('miles', 'meters', mile)
            self.assertEqual(meter, result)

class testYardsToMeters(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(4000,  3658.0), (64567, 59041.0),
                   (100000, 91441.0), (509175, 465595.0)]
    def testCorrectResult(self):
        for yard, meter in self.knownValues:
            result = conversions_refactored.allConversions('yards', 'meters', yard)
            self.assertEqual(meter, result)


class testYardsToMiles(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(4000,  2.0), (64567, 37.0),
                   (100000, 57.0), (509175, 289.0)]
    def testCorrectResult(self):
        for yard, mile in self.knownValues:
            result = conversions_refactored.allConversions('yards', 'miles', yard)
            self.assertEqual(mile, result)

class testMetersToMiles(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(10000,  6.0), (64567, 40.0),
                   (100000, 62.0), (5091754, 3164.0)]
    def testCorrectResult(self):
        for meter, mile in self.knownValues:
            result = conversions_refactored.allConversions('meters', 'miles', meter)
            self.assertEqual(mile, result)

class testMetersToYards(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(10000,  10936.0), (32, 35.0),
                   (96,105.0), (7559, 8267.0)]
    def testCorrectResult(self):
        for meter, yard in self.knownValues:
            result = conversions_refactored.allConversions('meters', 'yards', meter)
            self.assertEqual(yard, result)

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

class TestSameUnit(unittest.TestCase):
    units = ['celsius', 'farenheit', 'kelvin', 'yards', 'meters', 'miles']
    def testSameUnit(self):
        for unit in self.units:
            result = conversions_refactored.allConversions(unit, unit, 15)
            self.assertEqual(15, result)


if __name__ == "__main__":
    unittest.main()

