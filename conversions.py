#!user/bin/env python
# -*- coding: utf-8 -*-
"""Conversions"""

import decimal


ABSOLUTE_DIFFERENCE = 273.15

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
    deg_cel = degrees
    val_kelv = deg_cel + ABSOLUTE_DIFFERENCE

    return val_kelv

def convertCelciusToFarenheit(degrees):
    """Does math to return conversion from f to c as a decimal.
    Args:
        degrees (dec): degree to be converted.
    Returns:
        (dec) converted to celsius.
    Examples:
        fahrenheit_to_celsius(53)
        >>>> '11.66666666666666666666666667'
    """
    deg_far = degrees
    val_a = 32
    val_b = 1.8

    dec_val = ((deg_far * val_b) + val_a)

    return dec_val

print convertCelsiusToKelvin(555)