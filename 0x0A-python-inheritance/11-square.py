#!/usr/bin/python3

"""Class square that inherits from rectangle
   instantiation with size: def __init__(self, size)
   print() should print, and str() should return,
   the square description: [Square] <width>/<height>
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square that inherits from rectangle"""
    def __init__(self, size):
        """Initializes a square
           with the size of the
           square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
