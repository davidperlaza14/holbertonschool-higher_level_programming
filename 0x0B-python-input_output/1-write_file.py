#!/usr/bin/python3
"""Documentation for number_of_lines function"""


def write_file(filename="", text=""):
    """function that returns the number of lines of a text file
    """
    with open(filename, encoding='utf-8') as f:
        linenum = 0
        for l in f:
            linenum += 1
        return linenum
