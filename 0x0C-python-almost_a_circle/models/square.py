#!/usr/bin/python3

"""Module square that inherits from
   another rectangle class inside the
   package of models
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square inheriting from class
       Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square class with arguments
           size which is the size, x which is the x
           coordinate, y which is the y coordiate, and
           id which is the identity if the future
           square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Overloading method that prints
           string representation of a Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

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
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg

                elif pos == 1:
                    self.size = arg
                elif pos == 2:
                    self.x = arg
                elif pos == 3:
                    self.y = arg
                pos += 1

        elif kwargs and len(kwargs) != 0:

            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val

                elif key == "size":
                    self.size = val
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
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
