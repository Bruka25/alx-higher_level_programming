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
