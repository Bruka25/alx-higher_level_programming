#!/usr/bin/python3


"""Module that contains unittests for
   base class of the project

Unittest for the methods inside the class base
with the following modules:
    Test_instantiation
    Test_to_json_string
    Test_save_to_file
    Test_from_json_string
    Test_create
    Test_load_from_file
    Test_save_to_file_csv
    Tes_load_from_file_csv
"""
import os
import unittest
from os import path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_instantiation(unittest.TestCase):
    """Unittest for testing __init__ of the
       base class
    """

    def test_no_arguments(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(15, Base(15).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(15)
        b.id = 17
        self.assertEqual(17, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(15).__nb_instances)

    def test_string_id(self):
        self.assertEqual("Biruk", Base("Biruk").id)

    def test_float_id(self):
        self.assertEqual(7.5, Base(7.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_dictionary_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_boolean_id(self):
        self.assertEqual(False, Base(False).id)

    def test_list_id(self):
        self.assertEqual([1, 3, 4], Base([1, 3, 4]).id)

    def test_tuple_id(self):
        self.assertEqual((3, 3), Base((3, 3)).id)

    def test_set_id(self):
        self.assertEqual({1, 3, 4}, Base({1, 3, 4}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 3, 4}), Base(frozenset({1, 3, 4})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Biruk', Base(b'Biruk').id)

    def test_arraybyte_id(self):
        self.assertEqual((b'lmnopq'), Base(bytearray(b'lmnopq')).id)

    def test_viewmem_id(self):
        self.assertEqual((b'lmnopq'), Base(memoryview(b'lmnopq')).id)

    def test_id_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_id_nan(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(3, 4)


class Test_to_json_string(unittest.TestCase):
    """Class for Unittests for testing to_json_string
       method of Base class
    """

    def test_to_json_string_rect_type(self):
        rect = Rectangle(7, 4, 5, 3, 6)
        self.assertEqual(str, type(Base.to_json_string([
                                   rect.to_dictionary()])))

    def test_to_json_string_rect_one_dict(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_to_json_string_rect_two_dicts(self):
        rect1 = Rectangle(2, 3, 5, 19, 2)
        rect2 = Rectangle(4, 2, 4, 1, 12)
        lists = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lists)) == 106)

    def test_to_json_string_square_type(self):
        sqr = Square(7, 8, 4, 3)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

    def test_to_json_string_square_single_dict(self):
        sqr = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sqr.to_dictionary()])) == 39)

    def test_to_json_string_square_double_dicts(self):
        sqr1 = Square(10, 2, 3, 4)
        sqr2 = Square(4, 5, 21, 2)
        lists = [sqr1.to_dictionary(), sqr2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lists)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class Test_save_to_file(unittest.TestCase):
    """Class for unittests for testing save_to_file
       method of base class
    """

    @classmethod
    def delete_it(self):
        """Function that deletes any created files
           inside the method of save_to_file
        """
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_one_rect(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_to_file_two_rects(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file_one_sqr(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_two_sqrs(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(8, 1, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        sqr = Square(10, 7, 2, 8)
        Base.save_to_file([sqr])
        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_overwrite(self):
        sqr = Square(9, 2, 39, 2)
        Square.save_to_file([sqr])
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 4)


class Test_from_json_string(unittest.TestCase):
    """Class for Unittesting for testing from_json_string
       method of base class
    """

    def test_from_json_string_type(self):
        inputs = [{"id": 79, "width": 8, "height": 5}]
        json_inputs = Rectangle.to_json_string(inputs)
        outputs = Rectangle.from_json_string(json_inputs)
        self.assertEqual(list, type(outputs))

    def test_from_json_string_one_rect(self):
        inputs = [{"id": 79, "width": 8, "height": 5, "x": 6}]
        json_inputs = Rectangle.to_json_string(inputs)
        outputs = Rectangle.from_json_string(json_inputs)
        self.assertEqual(inputs, outputs)

    def test_from_json_string_two_rects(self):
        inputs = [
            {"id": 79, "width": 8, "height": 5, "x": 6, "y": 4},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_inputs = Rectangle.to_json_string(inputs)
        outputs = Rectangle.from_json_string(json_inputs)
        self.assertEqual(inputs, outputs)

    def test_from_json_string_one_sqr(self):
        inputs = [{"id": 79, "size": 4, "height": 5}]
        json_inputs = Square.to_json_string(inputs)
        outputs = Square.from_json_string(json_inputs)
        self.assertEqual(inputs, outputs)

    def test_from_json_string_two_sqrs(self):
        inputs = [
            {"id": 79, "size": 4, "height": 5},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_inputs = Square.to_json_string(inputs)
        outputs = Square.from_json_string(json_inputs)
        self.assertEqual(inputs, outputs)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 4)


class Test_create(unittest.TestCase):
    """Class for Unittesting for testing
       create method of Base class
    """

    def test_create_rect_original(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect1))

    def test_create_rect_new(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect2))

    def test_create_rect_is(self):
        rect1 = Rectangle(8, 5, 4, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertIsNot(rect1, rect2)

    def test_create_rect_equals(self):
        rect1 = Rectangle(8, 5, 4, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertNotEqual(rect1, rect2)

    def test_create_sqr_original(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sqr1))

    def test_create_sqr_new(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 1", str(sqr2))

    def test_create_sqr_is(self):
        sqr1 = Square(8, 5, 3, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertIsNot(sqr1, sqr2)

    def test_create_sqr_equals(self):
        sqr1 = Square(8, 5, 3, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertNotEqual(sqr1, sqr2)


class Test_load_from_file(unittest.TestCase):
    """Class Unittest for testing load_from_file_method
       of base class
   """

    @classmethod
    def delete_it(self):
        """Delete any created files of the
           load_from_file method
        """
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_load_from_file_first_rect(self):
        rect1 = Rectangle(8, 7, 3, 4, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        outputs = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(outputs[0]))

    def test_load_from_file_second_rect(self):
        rect1 = Rectangle(8, 7, 3, 4, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        outputs = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(outputs[1]))

    def test_load_from_file_rect_types(self):
        rect1 = Rectangle(8, 7, 3, 4, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_sqr(self):
        sqr1 = Square(1, 1, 4, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        outputs = Square.load_from_file()
        self.assertEqual(str(sqr1), str(outputs[0]))

    def test_load_from_file_second_sqr(self):
        sqr1 = Square(7, 1, 4, 3)
        sqr2 = Square(1, 7, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        outputs = Square.load_from_file()
        self.assertEqual(str(sqr2), str(outputs[1]))

    def test_load_from_file_square_types(self):
        sqr1 = Square(7, 1, 4, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        outputs = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in outputs))

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 3)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Class Unittests for testing save_to_file_csv
       method of base class
    """

    @classmethod
    def delete_it(self):
        """Deletes any created files"""
        try:
            os.remove("Base.csv")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rect(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8", file.read())

    def test_save_to_file_csv_two_rects(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", file.read())

    def test_save_to_file_csv_one_sqr(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file_csv_two_sqrs(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2\n3,8,1,2", file.read())

    def test_save_to_file__csv_cls_name(self):
        sqr = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sqr])
        with open("Base.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file_csv_overwrite(self):
        sqr = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sqr])
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 3)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Function for Unittesting for testing load_from_file_csv
       method of base class
    """

    @classmethod
    def delete_it(self):
        """Delete any created files."""
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        outputs = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(outputs[0]))

    def test_load_from_file_csv_second_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        outputs = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect2), str(outputs[1]))

    def test_load_from_file_csv_rect_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        outputs = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in outputs))

    def test_load_from_file_csv_first_sqr(self):
        sqr1 = Square(1, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        outputs = Square.load_from_file_csv()
        self.assertEqual(str(sqr1), str(outputs[0]))

    def test_load_from_file_csv_second_sqr(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(1, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        outputs = Square.load_from_file_csv()
        self.assertEqual(str(sqr2), str(outputs[1]))

    def test_load_from_file_csv_sqr_types(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        outputs = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in outputs))

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
