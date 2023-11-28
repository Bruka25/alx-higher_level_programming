#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_MaxInteger(unittest.TestCase):
    """
    A class to unitest a
    max integer module
    """

    def test_max_int(self):
        """
        Test the max integer in a list of integers whether
        they are positive or negative numbers
        """
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 7]), 7)
        self.assertAlmostEqual(max_integer([-4, -6, -2, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([-65, -110, -115, -130]), -65)
        self.assertAlmostEqual(max_integer([1.5, 2.5, 3.6, 6.7, 7.3]), 7.3)
        self.assertAlmostEqual(max_integer([8.8]), 8.8)

    def wrong_args(self):
        """
        Test the max integer with wrong
        arg types
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Biruk", 89, 34, -9.7, "Assefa"])

    def test_unordered(self):
        """Test an unordered list of ints"""
        un = [3, 7, 2, 1]
        self.assertEqual(max_integer(un), 7)

    def test_begginning(self):
        """Test a list with the max value
           at the begginnig of the list
        """
        begginning = [9, 2, 7, 4]
        self.assertEqual(max_integer(begginning), 9)

    def string_only(self):
        """Test only a list of strings"""
        string = ["Biruk", "Assefa", "Menkir", "Yabker"]
        self.assertEqual(max_integer(string), "Yabker")
