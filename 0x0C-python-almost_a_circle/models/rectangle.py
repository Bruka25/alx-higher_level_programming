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

    def update(self, *args, **kwargs):
        """Update with the given positional
           argument

        Args:
            *args type(int): Variable positional arguments
                -> Id attribute is the first argument
                -> Width attribute is the second
                -> Height attribute is the third
                -> x attribute is the fourth
                -> Y atttribute is the fifth
            **kwargs: Pointer to pointer to the key/value
                      pairs
        """
        if args and len(args) != 0:

            pos = 0
            for arg in args:
                if pos == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg

                elif pos == 1:
                    self.width = arg
                elif pos == 2:
                    self.height = arg
                elif pos == 3:
                    self.x = arg
                elif pos == 4:
                    self.y = arg
                pos += 1

        elif kwargs and len(kwargs) != 0:

            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val

                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Function that returns the dictionary representation
           of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
