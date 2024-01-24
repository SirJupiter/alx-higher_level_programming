#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""4-square.py

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

    @property
    def size(self):
        """Getter for the '__size' attribute. It allows read-only access

        Returns:
            the size value
        """
        return self.__size

    @size.setter
    def size(self, new_value):
        """Setter for the '__size' attribute. It allows
        modification of the __size attribute

        Args:
            new_value (int): value with which to set __size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(new_value) is not int:
            raise TypeError("size must be an integer")
        elif new_value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(new_value)

    def my_print(self):
        """function prints in stdout the square with the character '#'
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
