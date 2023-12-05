#!/usr/bin/python3

"""Function that appends a string at the
   end of file
"""


def append_write(filename="", text=""):
    """Append and write to the end with filename
       the name of the file and text the string of
       the file
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
