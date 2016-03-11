#!user/bin/env python
# -*- coding: utf-8 -*-
"""Conversions"""

import decimal


def convertCelsiusToKelvin(degrees):
    """"Does math to convert celsius to kelvin.
    Args:
        degrees (dec): degree in celsius to be converted.
    Returns:
        (dec) converted to kelvin.
    Examples:
        celsius_to_kelvin(100)
        >>> '373.15'
    """
    ABSOLUTE_DIFFERENCE = 273.15
    val_kelv = degrees + ABSOLUTE_DIFFERENCE

    return val_kelv

def convertCelsiusToFarenheit(degrees):
    """Does math to return conversion from c to f.
    """
    val_a = 32
    val_b = 1.8

    degrees = ((degrees * val_b) + val_a)

    return degrees

def convertFarenheitToCelsius(degrees):
    """Does math to return conversion from f to c.
    """
    val_a = 32
    val_b = 5
    val_c = 9

    degrees = ((degrees - val_a) * val_b) / val_c

    return degrees

def convertFarenheitToKelvin(degrees):
    """does math to return conv from f to k
    """
    cel = convertFarenheitToCelsius(degrees)
    kelv = convertCelsiusToKelvin(cel)
    return kelv

def convertKelvinToCelsius(degrees):
    """convert k to c"""
    ABSOLUTE_DIFFERENCE = 273.15
    val_cel = degrees - ABSOLUTE_DIFFERENCE
    return val_cel

def convertKelvinToFarenheit(degrees):
    """ convet k to f
    """
    degrees = convertKelvinToCelsius(degrees)
    degrees = convertCelsiusToFarenheit(degrees)
    return degrees

print convertKelvinToFarenheit(600)