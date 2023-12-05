#!/usr/bin/python3

"""Function that calculates pascals
   triangle
"""


def pascal_triangle(n):
    """Calculates pascals triange with
       n number of rows
       if n is less than or equal to 0
       function returns empty list
    """

    if n <= 0:
        return []

    maximum = n - 1
    tri = [[1]]

    for i in range(maximum):
        row = []
        row.append(1)

        if len(tri[i]) > 1:
            previous_row_len = len(tri[i]) - 1
            next_row = 1

            for j in range(previous_row_len):
                sum = tri[i][j] + tri[i][next_row]
                row.append(sum)
                next_row += 1

        row.append(1)
        tri.append(row)

    return tri
