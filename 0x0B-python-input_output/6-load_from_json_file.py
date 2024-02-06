#!/usr/bin/python3
"""Module contains 'load_from_json_file' function"""

from json import loads


def load_from_json_file(filename):
    """Function creates an Object from a JSON file

    Args:
        filename (file): JSON file
    """

    with open(filename, "r") as file:
        python_obj = loads(file.read())
        return python_obj
