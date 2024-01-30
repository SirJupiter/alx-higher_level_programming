#!/usr/bin/python3

"""Simple Rectangle Module"""


class Rectangle:
    """A class that defines a rectangle

    Attributes:
        number_of_instances (int): number of instances
        print_symbol (str): a print symbol
        width (int): width of rectangle
        height (int): height of rectangle
    """

    number_of_instances = 0  # public class attribute
    print_symbol = '#'  # public class attribute

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """prints the rectangle with the character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != (self.__height - 1):
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area

        Args:
            rect_1 (object): instance of Rectangle class
            rect_2 (object): instance of Rectangle class

        Raises:
            TypeError: if either of rect_1 and rect_2 is not
            an instance of Rectangle

        Returns:
            biggest rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_2.area() > rect_1.area():
                return rect_2
            return rect_1

    def square(cls, size=0):
        """Creates a new Rectangle instance with size
        equal to width equal to height

        Args:
            cls (int): cls
            size (int): size

        Returns:
            new Rectangle which is actually a square
        """

        newRectangle = Rectangle(int(cls), int(cls))
        return newRectangle
