#!/usr/bin/python3

"""Function that returns a dictionary description
   with simple data structure
"""


def class_to_json(obj):
    """Returns the dictionary description of
       parameter obj
    """
    return obj.__dict__
