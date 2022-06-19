#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends and returns the chars added quantity"""

    with open(filename, "a") as f:
        f.write(text)

        chars = len(text)
    return chars
