#!/usr/bin/python3

"""Function that reads a file prints
   to the stdout
"""


def read_file(filename=""):
    """read file and prints the contents in utf8 format"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
