#!/usr/bin/python3
"""Module contains class 'Square' that inherits from 'Rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class instantiates a square

    Attributes:
        size (int): size of one side of the square; private attribute.
    """

    def __init__(self, size):
        """Instantiation function

        Args:
            size (int): size of one side of the squar:
        """

        self.integer_validator("size", size)
        # Calling parent constructor with same value for width and height
        super().__init__(size, size)
        self.__size = size  # Private attribute
