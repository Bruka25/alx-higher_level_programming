#!/usr/bin/python3

"""A python module inside a python package models
   that represents the base for the other classes and
   models for the package to manage id attribute
   and avoid duplicate code the same code and
   bugs
"""

import json


class Base:
    """Defines a base moduele for the other
       python functions with a private class
       attribute __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the encoded json representation
           of python dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes json representation
           of list_objs to a file
        """

        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                return file.write(cls.to_json_string(None))

            attr_json = []

            for elements in list_objs:
                attr_json.append(elements.to_dictionary())

            return file.write(cls.to_json_string(attr_json))

    @staticmethod
    def from_json_string(json_string):
        """Static function that returns list of json string
           representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
