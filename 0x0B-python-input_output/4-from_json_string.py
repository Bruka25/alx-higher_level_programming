#!/usr/bin/python3

"""Function that returns an object represented
   by python
"""

import json


def from_json_string(my_str):
    """Returns the python representation of
       my_str from json
    """
    return json.loads(my_str)
