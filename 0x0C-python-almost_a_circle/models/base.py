#!/usr/bin/python3
"""Module contains Base class"""

import json
import csv
import turtle


class Base:
    """Base class for other classes in the hierarchy.

    Attributes:
        nb_objects (int): nb_objects # private class attribute
        id (int): id # public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Function to be called at instantiation

        Args:
            id (int): id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        json_string

        Args:
            json_string (JSON string): JSON string to be deserialized
        """
        if json_string is None or len(json_string) == 0:
            return []
        python_list = json.loads(json_string)

        return python_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            cls (class): class
            list_objs (list): list of instance objects of class
        """

        if list_objs is None:
            saved_list = []
        else:
            saved_list = []
            for obj in list_objs:
                saved_list.append(obj.__dict__)

        json_str = cls.to_json_string(saved_list)

        with open(f"{cls.__name__}.json",
                  "w", encoding='utf-8') as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary (dict): dictionary representation of an instance
            of a class
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(3, 5)
            else:
                dummy_instance = cls(3)
            dummy_instance.update(**dictionary)

            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances

        Exceptions:
            IOEror: if the .json file does not exist or cannot be opened
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r', encoding="utf-8") as file:
                python_object = cls.from_json_string(file.read())
                loaded_objects = (
                    [cls.create(**element) for element in python_object])
            return loaded_objects
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            list_objs (list): list of object instances to be serialized
        """

        with open(f"{cls.__name__}.csv", "w", newline="") as csv_file:
            if list_objs is None or len(list_objs) == 0:
                csv_file.write([])
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "width", "height", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in list_objs:
                    writer.writerow(row.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
