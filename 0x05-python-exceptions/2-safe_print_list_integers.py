#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    print the first function of a list
    and only integers
    """
    reply = 0

    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            reply += 1

        except (ValueError, TypeError):
            continue
    print("")

    return (reply)
