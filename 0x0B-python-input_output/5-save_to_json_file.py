#!/usr/bin/python3
"""Module contains 'save_to_json_file' function"""

from json import dump


def save_to_json_file(my_obj, filename):
    """Function writes an Object to a text file using JSON representation

    Args:
        my_obj (object): Python object
        filename (file): file into which JSON string will be written
    """

    with open(filename, "w", encoding="utf-8") as file:
        dump(my_obj, file)
