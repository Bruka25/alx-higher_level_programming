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
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = change_to_int(a)
    b = change_to_int(b)

    return a + b


def change_to_int(num):
    """Cast the data type of num argument

    Convert a float number to an int

    Args:
        num (:obj:`int, float`): The number to cast

    Returns:
         number to be casted to integer

    """

    if type(num) is float:
        num = int(num)
        return num

    return num
