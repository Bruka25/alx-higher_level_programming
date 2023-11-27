#!/usr/bin/python3

"""
This is init_board program
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard
Usage: nqueens N
N must be an integer greater or equal to 4
The program prints every possible solution to the problem
One solution per line
"""

import sys


def initialize_board(n):
    """Initialize an `n`x`n` sized chessboard
       with 0's
    """
    chess = []
    [chess.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chess]

    return chess


def deep_copy(chess):
    """Return a deepcopy of a
       chessboard
    """
    if isinstance(chess, list):
        return list(map(deep_copy, chess))
    return chess


def solved_board(chess):
    """Return the list of lists
       representation of a
       solved chessboard
    """
    solve = []

    for i in range(len(chess)):

        for j in range(len(chess)):
            if chess[i][j] == "Q":
                solve.append([i, j])
                break
    return solve


def x_board(chess, row, col):
    """X_board spots on a chessboard
       All spots where non-attacking
       queens can no longer be played are X-ed out

    Args:
        chess type(list): The current working chessboard
        row type(int): The row where a queen was last played
        col type(int): The column where a queen was last played
    """
    for j in range(col + 1, len(chess)):
        chess[row][j] = "x"
    # X out all backwards spots
    for j in range(col - 1, -1, -1):
        chess[row][j] = "x"
    # X out all spots below
    for i in range(row + 1, len(chess)):
        chess[i][col] = "x"
    # X out all spots above
    for i in range(row - 1, -1, -1):
        chess[i][col] = "x"
    # X out all spots diagonally down to the right
    j = col + 1
    for i in range(row + 1, len(chess)):
        if j >= len(chess):
            break
        chess[i][j] = "x"
        j += 1
    # X out all spots diagonally up to the left
    j = col - 1
    for i in range(row - 1, -1, -1):
        if j < 0:
            break
        chess[i][j]
        j -= 1
    # X out all spots diagonally up to the right
    j = col + 1
    for i in range(row - 1, -1, -1):
        if j >= len(chess):
            break
        chess[i][j] = "x"
        j += 1
    # X out all spots diagonally down to the left
    j = col - 1
    for i in range(row + 1, len(chess)):
        if j < 0:
            break
        chess[i][j] = "x"
        j -= 1


def solve_recursively(chess, row, queens, solve):
    """Solve an N-queens puzzle recursively

    Args:
        chess type(list): Current working chessboard
        row type(int): Current working row
        queens type(int): Current number of placed queens
        solutions type(list): List of lists of solutions.
    Returns:
        solve
    """

    if queens == len(chess):
        solve.append(solved_board(chess))
        return solve

    for j in range(len(chess)):

        if chess[row][j] == " ":
            temp = deep_copy(chess)
            temp[row][j] = "Q"
            x_board(temp, row, j)
            solve = solve_recursively(temp, row + 1, queens + 1, solve)

    return solve


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess = initialize_board(int(sys.argv[1]))
    solve = solve_recursively(chess, 0, 0, [])
    for non_sol in solve:
        print(non_sol)
