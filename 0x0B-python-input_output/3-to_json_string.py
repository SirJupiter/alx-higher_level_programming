#!/usr/bin/python3
"""Module contains 'to_json_string' function"""
from json import dumps


def to_json_string(my_obj):
    """Function returns a JSON representation of an object
    Function serializes a python object to a JSON-formatted string
    Args:
        my_obj (object): object  that will be converted into a string
        in JSON format.

    Returns:
        JSON representation of my_obj
    """
    json_string = dumps(my_obj)

    return json_string
