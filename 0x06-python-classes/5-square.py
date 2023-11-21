#!/usr/bin/python3

"""
Another square class based on the previous tasks

Size is private instance attribute
Error will be raised on invalid inputs
def area(self): returns size of area
Getters and setters for private instance attribute size

"""


class Square:

    """Class that defines a square by size
       def my_print(self): that prints in stdout
       the square with the character #
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

    def my_print(self):
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
