#!/usr/bin/python3

"""Formulates an inherited
   list class MyList
"""


class MyList(list):
    """Applies printing for
       list class
    """

    def print_sorted(self):
        """Prints a list in sorted
           and ascending order
        """
        print(sorted(self))
