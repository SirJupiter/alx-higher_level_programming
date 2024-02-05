#!/usr/bin/python3
"""Module contains 'is_kind_of_class' function"""


def is_kind_of_class(obj, a_class):
    """Check if an object belongs to a class or one of its subclasses.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if the object is an instance of the given class or any of
            its subclasses; False otherwise.
    """
    return isinstance(obj, a_class)
