#!/usr/bin/python3

"""
Another Rectangle class
The module provides a simple Rectangle class with
attribute width and height
Default value is 0
This function returns the area of a rectangle
print and str should print the rectangle
with the character #
repr should return string representation
del deletes an instance of a rectangle
Public class attribute number_of_instances initialized to 0

"""


class Rectangle:
    """Rectangle class with width and height,
       public instance methods area, perimeter,
       and with print, str, repr, and del
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):

        count = ""
        for i in range(self.__height):
            count += ("#" * self.__width)
            if i is not self.__height - 1:
                count += "\n"
        return count

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):

        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
