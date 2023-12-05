#!/usr/bin/python3

"""Function that inserts a line of text
   to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Insets a line of text with parameters filename,
       search_string, and new_string which is the appended
       string
    """

    with open(filename, mode='r', encoding='utf-8') as file:
        text = file.readlines()
        new_list = []

        for line in text:
            new_list.append(line)

            if search_string in line:
                new_list.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as wfile:
        for line in new_list:
            wfile.write(line)
