#!/usr/bin/python3
"""Module contains is_same_class function"""


def is_same_class(obj, a_class):
    """Check if obj belongs to class a_class.

    Args:
        obj (object instance): object from a class
        a_class (class): custom class
    """

    return type(obj) is a_class
