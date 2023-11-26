#!/usr/bin/python3

"""
This functions adds two integers

This function supplies one function, add_integer(a,b),
which adds together 2 int or float types
returns an integer
"""


def add_integer(a, b):
    """Return the sum of two integers or floats as an integer
       raises a TypeError for invalid argument type
    """
    add = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(add):
        return int(a) + int(b)

    for x, y in list(zip(add, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
