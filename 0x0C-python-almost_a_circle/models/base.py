#!/usr/bin/python3

"""A python module inside a python package models
   that represents the base for the other classes and
   models for the package to manage id attribute
   and avoid duplicate code the same code and
   bugs
"""

import json
from os import path
import csv
import turtle


class Base:
    """Defines a base moduele for the other
       python functions with a private class
       attribute __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the encoded json representation
           of python dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes json representation
           of list_objs to a file
        """

        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                return file.write(cls.to_json_string(None))

            attr_json = []

            for elements in list_objs:
                attr_json.append(elements.to_dictionary())

            return file.write(cls.to_json_string(attr_json))

    @staticmethod
    def from_json_string(json_string):
        """Static function that returns list of json string
           representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance with
           attributes all set
           **dictionary is double pointer to dict
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)
            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """Function that returns a list
           of instances
        """
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as file:
            objects = cls.from_json_string(file.read())
            inst = []

            for elements in objects:
                inst.append(cls.create(**elements))

            return inst

    @classmethod
    def load_from_file_csv(cls):
        """Function that deserializes a list of classes
           instantiated from a CSV file

        Returns:
            Empty list if the file does't exist
            Else return a list of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                lists = csv.DictReader(csv_f, fieldnames=fieldnames)
                lists = [dict([key, int(val)] for key, val in i.items())
                         for i in lists]
                return [cls.create(**i) for i in lists]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that Writes the CSV serialization of a list
           of objects to a file
           with arg list_objs which is a list of inherited
           Base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_f:
            if list_objs is None or list_objs == []:
                csv_f.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                output = csv.DictWriter(csv_f, fieldnames=fieldnames)
                for objects in list_objs:
                    output.writerow(objects.to_dictionary())


    @staticmethod
    def draw(list_rectangles, list_squares):
        """Function that Draws Rectangles and Squares
          using the turtle gui

          #FFA500 - Orange color for the rectangle
          #00FF00 - Green color for the square
        """
        draw_turt = turtle.Turtle()
        draw_turt.screen.bgcolor("#b7312c")
        draw_turt.pensize(3)
        draw_turt.shape("turtle")

        draw_turt.color("#FFA500")
        for r in list_rectangles:
            draw_turt.showturtle()
            draw_turt.up()
            draw_turt.goto(r.x, r.y)
            draw_turt.down()
            for i in range(2):
                draw_turt.forward(r.width)
                draw_turt.left(90)
                draw_turt.forward(r.height)
                draw_turt.left(90)
            draw_turt.hideturtle()

        draw_turt.color("#00FF00")
        for s in list_squares:
            draw_turt.showturtle()
            draw_turt.up()
            draw_turt.goto(s.x, s.y)
            draw_turt.down()
            for i in range(2):
                draw_turt.forward(s.width)
                draw_turt.left(90)
                draw_turt.forward(s.height)
                draw_turt.left(90)
            draw_turt.hideturtle()

        turtle.exitonclick()
