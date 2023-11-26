#!/usr/bin/python3

"""
This is a function that devides a matrix

This function takes in a list of lists matrix and divisor
All valid elements are divided by the divisor
After division a new matrix is created
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by `div`
    Matrix must be a list of lists
    Each sub-list must contain only integers or floats
    Empty sub-lists are not allowed
    Divisor must be greater than 0 and must be an int or float
    If the elemets are invalid a Type error will be raised
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(m) > 0 for m in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(m) == len(matrix[0]) for m in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not all(isinstance(x, (int, float)) for x in m):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    sub_matrix = []
    for m in matrix:
        sub_matrix.append(list(map(lambda n: round(n / div, 2), m)))

    return sub_matrix
