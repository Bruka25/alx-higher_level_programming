#!/usr/bin/python3

"""
Multiplies two matrcices using numpy
"""

import numpy

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy
       and return their multiplication

    Args:
        m_a is the first matrix
        m_b is the second matrix
    """

    return (numpy.matmul(m_a, m_b))
