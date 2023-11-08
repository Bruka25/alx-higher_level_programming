#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # multipy the values of a dictionary by 2
    return ({x: a_dictionary[x] * 2 for x in a_dictionary})
