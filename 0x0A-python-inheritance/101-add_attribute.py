#!/usr/bin/python3

"""Function that adds a new attribute
   to an object if it’s possible
"""


def add_attribute(obj, attr, val):
    """adds a new attribute to an object if it’s possible
       Raises a TypeError if if the object can’t have new attribute
       with parametrs of attritbute, object and value
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
