#!/usr/bin/python3

"""Simple Rectangle Module"""


class Rectangle:
    """A class that defines a rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle

        Returns:
            rectangle width
        """
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle

        Returns:
            rectangle height
        """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle

        Returns:
            area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter

        Returns:
            perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
