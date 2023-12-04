#!/usr/bin/python3

"""Function that adds a new attribute
   to an object if it’s possible
"""


def add_attribute(obj, attr, val):
    """adds a new attribute to an object if it’s possible
       Raises a TypeError if if the object can’t have new attribute
       with parametrs of attritbute, object and value
    """
    response = getattr(obj, "__doc__", None)
    if response is None:
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
