#!/usr/bin/python3
"""Module contains function that adds a new attribute to an object"""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute to the given object.

    Args:
        obj (object): The object to which we want to add a new attribute.
        attr_name (str): Name of the new attribute.
        value: Value for the new attribute.

    Raises:
        TypeError: if attribute cannot be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
