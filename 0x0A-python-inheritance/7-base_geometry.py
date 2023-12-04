#!/usr/bin/python3

"""
   Another geometry class based on the
   previous one
   public instance method: def area(self)
   Public instance method: def integer_validator(self, name, value):
   that validates value
"""


class BaseGeometry:
    """Defines a base geometry"""

    def area(self):
        """
        raises an Exception with the message area()
        is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter with args name (str)
           which is the name of the parameter and value
           (int) which is the parameter to validate
           Raises a TypeError if value is not an integer
           or ValueError if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
