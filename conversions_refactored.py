#!user/bin/env python
# -*- coding: utf-8 -*-
"""Conversions"""


class ConversionNotPossible(Exception):
    pass


def allConversions(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    value = float(value)


    if fromUnit == 'celsius':
        if toUnit == 'kelvin':
            ABSOLUTE_DIFFERENCE = 273.15
            value = value + ABSOLUTE_DIFFERENCE
            return value

        elif toUnit == 'farenheit':
            value = ((value * 1.8) + 32)
            return value
        else:
            raise ConversionNotPossible('Please enter the valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'farenheit':
        value = ((value - 32) * 5 / 9)
        if toUnit == 'celsius':
            return value
        elif toUnit == 'kelvin':
            return value + 273.15
        else:
            raise ConversionNotPossible('Please enter the valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'kelvin':
        value = value - 273.15
        if toUnit == 'celsius':
            return value
        elif toUnit == 'farenheit':
            value = ((value * 1.8) + 32)
            return value
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'miles':
        if toUnit == 'yards':
            pass
        elif toUnit == 'meters':
            pass
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'yards':
        if toUnit == 'meters':
            pass
        elif toUnit == 'miles':
            pass
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))
    if fromUnit == 'miles':
        if toUnit == 'meters':
            print 'You made it this far.'
        elif toUnit == 'yards':
            pass
        else:
            raise ConversionNotPossible('Please enter valid units to convert. You entered '
                                        'from {} to {}.'.format(fromUnit, toUnit))



print allConversions('farenheit', 'kelvin', 3)

