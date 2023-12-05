#!/usr/bin/python3

"""Function that writes a test file and
   returns the number of characters
   written
"""


def write_file(filename="", text=""):
    """returns the total of the number of
       lines, with filename the name of the
       file and text the string of the file
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
