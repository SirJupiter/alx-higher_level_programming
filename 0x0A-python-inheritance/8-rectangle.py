#!/usr/bin/python3
"""Module contains Rectangle class that inherits from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class instantiates a Rectangle

    Attributes:
        width (int): The length of the rectangle.
        height (int): The height of the rectangle.
        Both attributes are private
    """

    def __init__(self, width, height):
        """Instantiates on object from this class

        Args:
            width (int): The length of the rectangle.
            height (int): The height of the rectangle.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
