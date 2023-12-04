#!/usr/bin/python3

"""Class Rectangle that inherits
   from BaseGeometry
   area() method must be implemented
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ Intializes new rectangle With arguments
            width of the rectangle and height of
            the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of given rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str will return and print will
           print with the given description
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
