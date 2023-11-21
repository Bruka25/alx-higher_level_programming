#!/usr/bin/python3

"""
Another square class based on the previous tasks
Size is private instance attribute
Error will be raised on invalid inputs
def area(self): returns size of area
Getters and setters for private instance attribute size
def my_print(self): that prints in stdout the square with the character #

"""


class Square:

    """
    Class that defines a square by size, which defaults 0
    if size is equal to 0 print an empty line
    position must be a tuple of 2 positive integers
    position should be use by using space
    lines should not be filled by spaces
    when position[1] > 0
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        return (self.get_str())

    def area(self):
        return self.__size * self.__size

    def get_str(self):
        count = ""
        if self.__size == 0:
            count += "\n"
            return count
        for i in range(self.__position[1]):
            count += "\n"
        for i in range(self.__size):
            count += (" " * self.__position[0])
            count += ("#" * self.__size)
            if i is not (self.__size - 1):
                count += "\n"
        return count

    def my_print(self):
        print(self.get_str())
