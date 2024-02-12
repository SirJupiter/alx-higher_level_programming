"""Module contains class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Initializes a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a square object"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Public getter that retrieves the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Public setter sets the size of the square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the class Square by assigning attributes

        Args:
            *args (tuple of ints): list of no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute

            **kwargs (dict): keyworded arguments
        """

        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                else:
                    self.y = value

    def to_dictionary(self):
        """Return a dictionary representation of this object."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """Prints a string of information when print() is called"""
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")
