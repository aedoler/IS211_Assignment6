
import unittest
import conversions_refactored


class testCelsiusToKelvin(unittest.TestCase):
    """Tests that each conversions is working properly and that an
    error is thrown when necessary"""
    knownValues = [(0, 273.15), (50, 323.15), (100, 373.15), (555, 828.15)]
    def testCelsiusToKelvin(self):
        """convertCelsiusToKelvin should return the correct value"""
        for cel, kel in self.knownValues:
            result = conversions_refactored.allConversions('celsius', 'kelvin', cel)
            self.assertEqual(kel, result)

class testCelsiusToFarenheit(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(0, 32.0), (16, 60.8), (27, 80.6), (17, 62.6)]
    def testCorrectResult(self):
        for cel, far in self.knownValues:
            result = conversions_refactored.convertCelsiusToFarenheit('celsius', 'farenheit', cel)
            self.assertEqual(far, result)

class testFarenheihtToCelsius(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(32, 0), (64, 17), (80, 26), (88, 31)]
    def testCorrectResult(self):
        for far, cel in self.knownValues:
            result = conversions_refactored.convertFarenheitToCelsius('farenheit', 'celsius', far)
            self.assertEqual(cel, result)

class testFarenheihtToKelvin(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(3, 256.15), (5, 258.15), (100, 310.15), (4444, 2724.15)]
    def testCorrectResult(self):
        for far, kel in self.knownValues:
            result = conversions_refactored.convertFarenheitToKelvin('farenheit', 'kelvin', far)
            self.assertEqual(kel, result)

class testKelvinToCelsius(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(402, 128.85000000000002), (350, 76.85000000000002), (1000, 726.85), (800, 526.85)]
    def testCorrectResult(self):
        for kel, cel in self.knownValues:
            result = conversions_refactored.convertKelvinToCelsius('kelvin', 'celsius', kel)
            self.assertEqual(cel, result)

class testKelvinToFarenheit(unittest.TestCase):
    """convertCelsiusToFarenheit should return the correct value"""
    knownValues = [(300, 80.33000000000004), (270, 26.33000000000004),
                   (455, 359.33000000000004), (600, 620.33)]
    def testCorrectResult(self):
        for kel, far in self.knownValues:
            result = conversions_refactored.convertKelvinToFarenheit('kelvin', 'farenheit', kel)
            self.assertEqual(far, result)


if __name__ == "__main__":
    unittest.main()