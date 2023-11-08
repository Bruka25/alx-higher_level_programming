#!/usr/bin/python3

# returns a list multiplied by a number
def mutiply_list_map(my_list=[], number=0):
    return (list(map(lambda n: n * number, my_list)))
