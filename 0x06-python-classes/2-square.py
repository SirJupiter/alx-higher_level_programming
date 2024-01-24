#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""2-square.py

Module contains class Square that defines a square
"""


class Square:
    """Square class represents a square

    Attributes:
        side (int): size of the square - private attribute
    """
    def __init__(self, size=0):
        """Initialize square with given 'size' or set it to 0 if
        no argument is passed

        Args:
            size (int): size of the square passed to instance
        """

        self.__size = size  # Private attribute
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
