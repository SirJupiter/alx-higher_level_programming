#!/usr/bin/python3

"""Module for integer addition"""


def add_integer(a, b=98):
    """Function adds two integers

    Args:
        a (int): first integer
        b (int): second integer

    Raises:
        TypeError:  If either 'a' or 'b' is not an integer.

    Returns:
        The addition of a and b
    """

    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
