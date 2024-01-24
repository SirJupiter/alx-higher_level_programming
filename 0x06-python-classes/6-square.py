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
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with given 'size' or set it to 0 if
        no argument is passed

        Args:
            size (int): size of the square
            position (:obj:'tuple'): position of square elements

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        self.__size = size  # private attribute
        self.__position = position  # private attribute
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

    @property
    def position(self):
        """Getter for the '__position' attribute. It allows read-only access

        Returns:
            the position tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the '__position' attribute. It allows
        modification of the __position attribute

        Args:
            value (tuple): tuple of 2 integers to set __position

        Raises:
            TypeError: if size is not an integer
        """

        if type(value) is not tuple:
            raise TypeError("position must be a tuple of two integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of two integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of two integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of two integers")
        else:
            self.__position = value

    def my_print(self):
        """function prints in stdout the square with the character '#'
        """
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print()
