#!/usr/bin/python3

"""
Another square class based on the previous tasks

Size is private instance attribute
Error will be raised on invalid inputs
def area(self): returns size of area
"""


class Square:

    """Class that defines a square by size
       and also compares two squares based
       on the given size
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __lessThan__(self, other):
        return self.__size < other.size

    def __lessOrEqual__(self, other):
        return self.__size <= other.size

    def __equal__(self, other):
        return self.__size == other.size

    def __negate__(self, other):
        return self.__size != other.size

    def __greater__(self, other):
        return self.__size > other.size

    def __greaterOrEqual__(self, other):
        return self.__size >= other.size
