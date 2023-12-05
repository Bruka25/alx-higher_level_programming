#!/usr/bin/python3

"""Module that defines students with
   public instance attributes first_name
   last_name, age
   with Public method def to_json(self, attrs=None)
   If attrs is a list of string, only attribute names
   contained in the list must be retrieved
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

    def to_json(self, attrs=None):
        "return dictionary representation of student"""

        dic = self.__dict__
        empty_dic = dict()

        if type(attrs) is list:

            for a in attrs:
                if type(a) is not str:
                    return dic

                if a in dic:
                    empty_dic[a] = dic[a]

            return empty_dic

        return dic
