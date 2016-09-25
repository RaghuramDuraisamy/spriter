# -*- coding: utf-8 -*-
import unittest

from spriter.image import BaseImage, class_name_function


class TestBaseImage(unittest.TestCase):

    def test_default_class_name(self):
        image = BaseImage("a.png", "abc")
        self.assertEqual(image.class_name, "abc")

    def test_class_name_based_in_path(self):
        image = BaseImage("a.png")
        self.assertEqual(image.class_name, "sa")

    def test_class_name_function_override(self):
        func = lambda x: "s" + x
        image = BaseImage("a.png", class_name_function=func)
        self.assertEqual(image.class_name, "sa.png")

    def test_class_name_function_only_number(self):
        image = BaseImage("123.png")
        self.assertEqual(image.class_name, "s123")

    def test_class_name_function_first_letter_is_number(self):
        image = BaseImage("1s2aaa3.png")
        self.assertEqual(image.class_name, "s1s2aaa3")

    def test_class_name_function(self):
        name = class_name_function("1$sôf.")
        self.assertEqual(name, "s1-sf")
