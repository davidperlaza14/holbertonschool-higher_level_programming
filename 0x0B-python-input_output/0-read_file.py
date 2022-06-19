#!/usr/bin/python3
"""Documentation for read_file function"""


def read_file(filename=""):
    """Function that reads the file and prints
    """

    with open(filename, encoding='utf-8') as f:
        for l in f:
            print(l, end="")
