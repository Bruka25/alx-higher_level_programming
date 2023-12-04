#!/usr/bin/python3
"""
A function that returns if object is an
instance of a class
obj() is the object to check
a_class() class to match the type
obj to
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the instance matches
       otherwise returns False
    """
    return isinstance(obj, a_class)
