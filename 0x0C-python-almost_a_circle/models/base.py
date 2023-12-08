#!/usr/bin/python3

"""A python module inside a python package models
   that represents the base for the other classes and
   models for the package to manage id attribute
   and avoid duplicate code the same code and
   bugs
"""


class Base:
    """Defines a base moduele for the other
       python functions with a private class
       attribute __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
