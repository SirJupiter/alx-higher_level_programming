#!/usr/bin/python3
"""Module contains 'from_json_string' function"""

from json import loads


def from_json_string(my_str):
    """Function returns an object(Python data structure)
    represented by a JSON string

    Args:
        my_str (str): JSON string to be deserialized

    Returns:
        python_object: python object with python data structure
    """

    python_object = loads(my_str)
    return python_object
