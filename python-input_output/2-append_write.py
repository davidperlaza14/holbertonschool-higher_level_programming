#!/usr/bin/python3
"""append_write
"""


def append_write(filename="", text=""):
    """Append - will append to the end of the file
    """

    with open(filename, mode="a", encoding="utf-8") as appendFile:
        appendFile.write(text)
        return len(text)
