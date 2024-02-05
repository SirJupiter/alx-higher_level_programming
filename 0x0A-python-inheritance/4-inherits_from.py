#!/usr/bin/python3
"""Module contains 'inherits_from' function"""


def inherits_from(obj, a_class):
    """Check if an object is derived from another class.

    Args:
        obj (object): The object to check for inheritance.
        a_class (type): The base class or parent class to compare against.

    Returns:
        bool: True if the object is derived from 'a_class', False otherwise.

    Raises:
        TypeError: If either argument is not of type 'object' or 'type'.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
