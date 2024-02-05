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
