#!/usr/bin/python3

"""Function that writes a test file and
   returns the number of characters
   written
"""


def number_of_lines(filename=""):
    """returns the total of the number of
       lines, with filename the name of the
       file
    """

    total = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            total += 1
    return total
