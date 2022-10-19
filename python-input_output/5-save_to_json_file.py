#!/usr/bin/python3
"""to_json_string
"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as saveFile:
        json.dump(my_obj, saveFile)