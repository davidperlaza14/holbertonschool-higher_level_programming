#!/usr/bin/python3
"""Function that returns the Pascal's triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal's triangle of n"""

    pt = []

    if n <= 0:
        return pt

    if n == 1:
        pt = [[1]]
        return pt

    """list containing the first two lines"""
    pt = [[1], [1, 1]]

    """This loop is generated as many times as there are lines."""
    for prev_val in range(1, n - 1):

        """The line is initialized"""
        line = [1]

        """Loop generated for each of the vals in the previous line"""
        for nxt_val in range(0, len(pt[prev_val]) - 1):

            """New vals are added to the list"""
            """The previous val is added to the next val in the list"""
            line.extend([pt[prev_val][nxt_val] + pt[prev_val][nxt_val + 1]])

        """The constant '1' is added at the end of the list."""
        line += [1]

        """The list is fill with the line"""
        pt.append(line)

    return pt
