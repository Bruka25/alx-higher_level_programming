#!/usr/bin/python3

"""Formulates an inherited list
   class MyList
"""


class MyList(list):
    """ Implements sorted printing for
        the for list class
    """

    def print_sorted(self):
        """Print a list but in ascending
           sorted order
        """
        print(sorted(self))
