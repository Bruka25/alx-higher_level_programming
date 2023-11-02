#!/usr/bin/env python3

from magic_calculation_102 import add, sub

# perform claclulation based on given bytecode


def magic_calculation(a, b):
    if (a < b):
        calculate = add(a, b)

        for num in range(4, 6):
            calculate = add(calculate, num)

        return calculate
    else:
        return sub(a, b)
