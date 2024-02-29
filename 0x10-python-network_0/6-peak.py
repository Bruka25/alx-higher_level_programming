#!/usr/bin/python3
"""Python program for finnding the peak number
   from a list of integers
"""


def find_peak(list_of_integers):
    """ Function that findsa peak in a list of
        unsorted integers
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    middle = int(size / 2)
    peak_int = list_of_integers[middle]
    if peak_int > list_of_integers[middle - 1] and peak_int > list_of_integers[middle + 1]:
        return peak_int
    elif peak_int < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
