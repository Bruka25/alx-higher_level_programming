#!/usr/bin/python3
"""
Module for unittesting that tests differents behaviors
of the Square class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
       Class to test the different conditions
       of Square Class
    """

    def test_getter(self):
        sqr1 = Square(8)
        self.assertEqual(sqr1.size, 8)

    def test_setter(self):
        sqr1 = Square(8)
        sqr1.size = 4
        self.assertEqual(sqr1.size, 4)

    def test_string(self):
        sqr1 = Square(3)

        with self.assertRaises(TypeError):
            sqr1.size = "Biruk"

    def test_negative(self):
        sqr1 = Square(4)

        with self.assertRaises(ValueError):
            sqr1.size = -7

    def test_zero(self):
        sqr1 = Square(6)

        with self.assertRaises(ValueError):
            sqr1.size = 0

    def test_decimal(self):
        sqr1 = Square(3)

        with self.assertRaises(TypeError):
            sqr1.size = 3.6

    def test_tuple(self):
        sqr1 = Square(9)

        with self.assertRaises(TypeError):
            sqr1.size = (4, 7)

    def test_empty(self):
        sqr1 = Square(3)

        with self.assertRaises(TypeError):
            sqr1.size = ''

    def test_none(self):
        sqr1 = Square(7)

        with self.assertRaises(TypeError):
            sqr1.size = None

    def test_list(self):
        sqr1 = Square(5)

        with self.assertRaises(TypeError):
            sqr1.size = [5, 7]

    def test_dict(self):
        sqr1 = Square(5)

        with self.assertRaises(TypeError):
            sqr1.size = {"Hello": 5, "Yabker": 8}

    def test_width(self):
        sqr1 = Square(7)
        sqr1.size = 6
        self.assertEqual(sqr1.width, 6)
        self.assertEqual(sqr1.height, 6)

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0

        sqr1 = Square(6, 5, 4, 11)
        sqr1_dictionary = sqr1.to_dictionary()
        new_sqr = {'id': 11, 'x': 5, 'size': 6, 'y': 4}
        self.assertEqual(sqr1_dictionary, new_sqr)

        sqr1 = Square(4, 0, 0, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        new_sqr = {'id': 7, 'x': 0, 'size': 4, 'y': 0}
        self.assertEqual(sqr1_dictionary, new_sqr)

        sqr1.update(7, 6, 3, 2)
        sqr1_dictionary = sqr1.to_dictionary()
        new_sqr = {'id': 7, 'x': 2, 'size': 6, 'y': 0}
        self.assertEqual(sqr1_dictionary, new_sqr)
