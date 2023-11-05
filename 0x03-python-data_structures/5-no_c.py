#!/usr/bin/python3

def no_c(my_string):
    remove = ''

    for char in my_string:
        if char != 'c' and char != 'C':
            remove += char

    return remove
