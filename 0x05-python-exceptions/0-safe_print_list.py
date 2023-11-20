#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    index = 0

    try:
        for j in my_list:
            if idx < x:
                print('{}'.format(my_list[index]), end='')
                index += 1

        print()
    except TypeError:
        pass
    finally:
        return index
