#!/usr/bin/python3

"""
The function is called say my name function

say my name function takes one required parameter and other optional
Prints "My name is (first) (last)"
(first) and (last) are the arguments of the function
"""


def say_my_name(first_name, last_name=""):
    """Print My name is (first) (last)
       else raise a typeerror
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
