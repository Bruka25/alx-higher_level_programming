#!/usr/bin/python3

"""
Another square class based on the previous tasks

Size is private instance attribute
Error will be raised on invalid inputs
def area returns size of area
"""


class Square:
    """ Class that defines a square by size
        and can compute area
    """

    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        return self.__size * self.__size
