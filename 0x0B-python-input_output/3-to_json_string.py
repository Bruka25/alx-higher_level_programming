#!/usr/bin/python3

"""Function that returns the json
   representation of an object
"""

import json


def to_json_string(my_obj):
    """Returns the json representation of
       my_obj
    """
    return json.dumps(my_obj)
