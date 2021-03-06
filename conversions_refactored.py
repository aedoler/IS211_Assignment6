#!user/bin/env python
# -*- coding: utf-8 -*-
"""Conversions"""


class ConversionNotPossible(Exception):
    pass



def allConversions(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    value = float(value)
    if fromUnit == toUnit:
        value = value
        return value

    if fromUnit == 'celsius':
        if toUnit == 'kelvin':
            ABSOLUTE_DIFFERENCE = 273.15
            value = value + ABSOLUTE_DIFFERENCE
            return round(value)

        elif toUnit == 'farenheit':
            value = ((value * 1.8) + 32)
            return round(value)
        else:
            raise ConversionNotPossible('Please enter the valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'farenheit':
        value = ((value - 32) * 5 / 9)
        if toUnit == 'celsius':
            return round(value)
        elif toUnit == 'kelvin':
            return round(value + 273.15)
        else:
            raise ConversionNotPossible('Please enter the valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'kelvin':
        value = value - 273.15
        if toUnit == 'celsius':
            return round(value)
        elif toUnit == 'farenheit':
            value = ((value * 1.8) + 32)
            return round(value)
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'miles':
        if toUnit == 'yards':
            value = value * 1760.0
            return round(value)
        elif toUnit == 'meters':
            value = value / 0.00062137
            return round(value)
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'yards':
        if toUnit == 'meters':
            value = value / 1.0936
            return round(value)
        elif toUnit == 'miles':
            value = value / 1760.0
            return round(value)
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'meters':
        if toUnit == 'miles':
            value = value * 0.00062137
            return round(value)
        elif toUnit == 'yards':
            value = value * 1.0936
            return round(value)
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))



print allConversions('yards', 'yards', 1678)


