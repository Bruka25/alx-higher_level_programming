#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        return

    div_list = []
    for x in my_list:
        if x % 2 == 0:
            div_list.append(True)
        else:
            div_list.append(False)
    return div_list
