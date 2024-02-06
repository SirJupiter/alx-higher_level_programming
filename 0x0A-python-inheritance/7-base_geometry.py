#!/usr/bin/python3
"""Module contains BaseGeometry class"""


class BaseGeometry:
    """Base class for all geometrical shapes.

    Attributes:
    """

    def area(self):
        """Calculates the area of the shape.
        Raises:
            Exception: exception with a particular message
        """

        raise Exception("area()is not implemented")

    def integer_validator(self, name, value):
        """Function validates value

        Args:
            name (str): name string
            value (int): integer value

        Raises:
            TypeError Exception: if value is not integer
            ValueError Exception: if value is less or equal to 0
        """

        if type(value) is not int:
            error_message = f"{name} must be an integer"
            raise TypeError(error_message)

        if value <= 0:
            error_message = f"{name} must be greater than 0"
            raise ValueError(error_message)
