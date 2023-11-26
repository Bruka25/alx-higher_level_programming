#!/usr/bin/python3

"""
This function multipilies two matrices
prototype of the function def matrix_mul(m_a, m_b):
m_a and m_b must be an list of lists of integers
or floats
Raises a typeerror if invalid arguments are given
Returns new matrix of  the multiplication of m_a by m_b
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a is the first matrix.
        m_b is the second matrix
    Raises type error in the following conditions
        If either m_a or m_b is not a list of lists of ints/floats
        If either m_a or m_b is empty
        If either m_a or m_b has different-sized rows
        And valueerror If m_a and m_b cannot be multiplied
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_inv = []

    for i in range(len(m_b[0])):

        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        matrix_inv.append(new_row)

    new_matrx = []

    for row in m_a:
        new_row = []

        for col in matrix_inv:
            product = 0
            for p in range(len(inverted_b[0])):
                product += row[p] * col[p]
            new_row.append(product)
        new_matrx.append(new_row)

    return new_matrx
