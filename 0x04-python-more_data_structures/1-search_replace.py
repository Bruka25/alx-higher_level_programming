#!/usr/bin/python3

# search and replace x
def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]
