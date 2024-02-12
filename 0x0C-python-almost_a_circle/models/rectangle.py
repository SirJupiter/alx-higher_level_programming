#!/usr/bin/python3
"""Model contains Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class for instantiating a rectangle

    Private instance attributes:
        __width (int): the width of the rectangle
        __height(int): the height of the rectangle
        __x (int): x
        __y (int): y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle object

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x
            y (int): y
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        # if isinstance(id, int):
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets the x value of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__width = x

    @property
    def y(self):
        """Gets the y value of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Retrieve the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display a representation of the rectangle with '#'"""
        if self.__width == 0 or self.__height == 0:
            print()
            return

        if self.y > 0:
            [print() for y_y in range(self.y)]
        for h in range(self.__height):
            [print(" ", end="") for x_x in range(self.x)]
            [print('#', end="") for x in range(self.__width)]
            print()

    def update(self, *args, **kwargs):
        """Updates the class Rectangle by assigning an argument
        to each attribute:

        Args:
            *args (tuple of ints): list of arguments
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute

            **kwargs (dict): keyword arguments
        """
        if args and args[0] is not None:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.width = args[1]

            if len(args) >= 3:
                self.height = args[2]

            if len(args) >= 4:
                self.x = args[3]

            if len(args) == 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                else:
                    self.y = value

    def to_dictionary(self):
        """Return a dictionary representation of this object."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """Prints a string when print() is called"""
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")
