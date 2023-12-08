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
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)
