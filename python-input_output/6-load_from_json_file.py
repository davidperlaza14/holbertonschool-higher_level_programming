#!/usr/bin/python3
"""save_to_json_file
"""


import json


def load_from_json_file(filename):
    """Writes an object to a text file, using JSON
    """

    with open(filename, mode="r", encoding="UTF-8") as loadFile:
        json.load(loadFile)
