#!/usr/bin/python3
"""Module contains 'class_to_json' function"""


def class_to_json(obj):
    """Converts a Python object to JSON.

    Args:
        obj (object): The Python object to convert to JSON.

    Returns:
        str: A string representation of the JSON object.

    Raises:
        TypeError: If `obj` is not an instance of a class or
        if it does not have a `__dict__`.
    """

    if not hasattr(obj, "__dict__"):
        raise Exception("object not serializable")

    python_object = obj.__dict__

    return python_object
