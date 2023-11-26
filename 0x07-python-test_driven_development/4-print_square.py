#!/usr/bin/python3

"""
This function Prints Square
The Print Square function prints a square with "#"
The args given should determine the
width or height of square
"""


def print_square(size):
    """Print a perfect square given a valid int or
       float argument
       Otherwise raise a typeerror
    """

    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size))
