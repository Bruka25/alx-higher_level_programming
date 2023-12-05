#!/usr/bin/python3

"""Module that defines students with
   public instance attributes first_name
   last_name, age
"""


class Student:
    """Class that tells students first name
       last name and age as its parameters
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates a class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        "return dictionary representation of student"""
        return self.__dict__
