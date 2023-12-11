#!/usr/bin/python3
"""
A module that test differents behaviors
of the base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRect(unittest.TestCase):
    """
    Class to test different cases of
    rectangle Class
    """

    def test_rect_subclass(self):
        """
        Function that Tests the inheritance
        from base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """
        Function that test parameters for
        rectangle class
        """
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        rect3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(rect1.id, 42)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect2.id, 43)
        self.assertEqual(rect2.width, 2)
        self.assertEqual(rect2.height, 10)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)
        self.assertEqual(rect3.id, 12)
        self.assertEqual(rect3.width, 10)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 0)
        self.assertEqual(rect3.y, 0)

        with self.assertRaises(TypeError):
            rect4 = Rectangle()

    def test_string(self):
        """
        Function that tests string parameters
        for a rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle('Biruk', 'Assefa')

    def test_type_parameters(self):
        """
        Function that tests different types of parameters
        for a rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle(3.3, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-2342, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 5)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(False, 8)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(5, 4.76)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, "Yabker")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(7, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(8, -479)
            raise ValueError

        with self.assertRaises(TypeError):
            Rectangle(4, 5, 1.60)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(7, 9, "Biruk")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(3, 6, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(3, 6, -47985)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(6, 3, 3, 6.53)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(7, 5, 3, "Biruk")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(2, 8, 4, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(2, 3, 6, -47)
            raise ValueError()
