#!/usr/bin/python3
"""
Checks if an object is inherited directly
or indirectly from a given class
obj() is the object to check
a_class() class to match the type
obj to
"""


def inherits_from(obj, a_class):
    """If the object is inherited return True
       otherwise return False
    """
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)

    return False
