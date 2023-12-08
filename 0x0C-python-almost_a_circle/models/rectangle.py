#!/usr/bin/python3

"""This module represents a rectangle class for
    the models package
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from the
       base class of another  module inside the
       package of models
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle class with arguments
           width, height, x coordinate, y coordinate, and
           id of the rectangle
           Returns TypeError if the parameters are not
           integers
           Raises ValueError if width or height are <= 0
           Raises ValueError if y or x are < 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Returns the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Returns x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Returns y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Function that Returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Function that Print Rectangle instance to
           the stdout using `#` character
        """

        if self.width == 0 or self.height == 0:
            print("")
            return

        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """Method that will be ovverirded to return
           the given output
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height
        )
