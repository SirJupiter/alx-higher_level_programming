#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""3-square.py

Module contains class that defines a square
"""


class Square:
    """This class represents a square

    Attributes:
        __size (int): size of square - private attribute
    """
    def __init__(self, size=0):
        """Initialize square with given 'size' or set it to 0 if
        no argument is passed

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        self.__size = size  # private attribute
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square

        Returns:
            area of the square
        """

        return self.__size ** 2
