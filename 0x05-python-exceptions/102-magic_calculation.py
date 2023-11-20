#!/usr/bin/python3

def magic_calculation(a, b):
    """
    magic calculation based on
    a given bytecode
    """

    output = 0

    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            else:
                output += a ** b / num
        except:
            output = b + a
            break

    return (output)
