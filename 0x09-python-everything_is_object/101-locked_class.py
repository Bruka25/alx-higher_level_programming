#!/usr/bin/python3

"""Defines a locked class
   It prevents the user from dynamically creating new instance attributes,
   except if the new instance attribute is called first_name
"""


class LockedClass:
    """
    Prevents users from making new instances
    """

    __slots__ = ["first_name"]
