#!/usr/bin/python3

""" Executes a class checking
    function
    obj() is the object to check
    a_class() class to match the type
    obj to
"""


def is_same_class(obj, a_class):
    """Returns True if a class is an exact instance of
       a class, if not it will return False
    """
    if type(obj) == a_class:
        return True

    return False
