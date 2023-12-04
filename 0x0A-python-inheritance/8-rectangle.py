#!/usr/bin/python3

"""Class Rectangle that inherits
   from BaseGeometry
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
