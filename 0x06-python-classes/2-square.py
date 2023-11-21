#!/usr/bin/python3
"""
This is Square class

This module provides a simple Square class with init size
Size is private instance attribute
Errors will be raised for invalid input
"""


class Square:

    """Class that defines a square by
    init size
    """
    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
