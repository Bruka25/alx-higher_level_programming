#!/usr/bin/python3

import math


"""
This magicClass does exactly what the provided
bytecode does
"""


class MagicClass:
    """
    Repr a circle
    with attributes
    """

    def __init__(self, radius=0):
        """Initialize a MagicClass
        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the
           circle
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference
           of the circle
        """
        return (2 * math.pi * self.__radius)
