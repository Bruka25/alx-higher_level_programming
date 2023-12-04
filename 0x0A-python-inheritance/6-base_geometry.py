#!/usr/bin/python3

"""
   Another geometry class based on the
   previous one
   public instance method: def area(self)
"""


class BaseGeometry:
    """Defines a base geometry"""

    def area(self):
        """
        raises an Exception with the message area()
        is not implemented
        """
        raise Exception("area() is not implemented")
