#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    row = 0
    for i in matrix:
        for j in matrix[row]:
            print("{:d}".format(j), end="")
            if j != matrix[row][-1]:
                print(" ", end="")
        print("")
# increment to the next row
        row += 1
