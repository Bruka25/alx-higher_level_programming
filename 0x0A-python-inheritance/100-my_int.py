#!/usr/bin/python3

"""
   Class that that inherits from
   int
"""


class MyInt(int):
    """MYInt class that inherits from int"""
    def __eq__(self, other):
        """Magic function that overrides ==
           with !=
        """
        return self - other != 0

    def __ne__(self, other):
        """Magic function that overrides
           != with ==
        """
        return self - other == 0
