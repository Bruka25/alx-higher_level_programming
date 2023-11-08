#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.items())

# sort keys alphabetically inside dictionary
    for a, b in sort:
        print('{0}: {1}'.format(a, b))
