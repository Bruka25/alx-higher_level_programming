#!/usr/bin/python3

"""Function that writes object to text file
   using json
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to text using json
       with parameters my_obj and
       filename
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
