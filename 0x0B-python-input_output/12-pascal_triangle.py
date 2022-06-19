#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    dalis = [[0 for x in range(i + 1)] for i in range(n)]
    dalis[0] = [1]

    for dalis in range(1, n):
        dalis[i][0] = 1
        for j in range(1, i + 1):
            if j < len(dalis[i - 1]):
                dalis[i][j] = dalis[i - 1][j - 1] + dalis[i - 1][j]
            else:
                dalis[i][j] = dalis[i - 1][0]
    return dalis
