#!/usr/bin/python3

"""Function that loads creates an
   object from json file
"""
import json


def load_from_json_file(filename):
    """load the json file of the
       filename parameter
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
