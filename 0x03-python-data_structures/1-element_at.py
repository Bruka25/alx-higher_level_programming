#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
# if the element is negative or out of range return None

    return my_list[idx]
