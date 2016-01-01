#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject2(Koan):
    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        with self.assertRaises(TriangleError):
            triangle2(0, 0, 0)

        with self.assertRaises(TriangleError):
            triangle2(3, 4, -5)

        with self.assertRaises(TriangleError):
            triangle2(1, 1, 3)

        with self.assertRaises(TriangleError):
            triangle2(2, 5, 2)

    def test_equilateral_triangles_have_equal_sides(self):
        self.assertEqual('equilateral', triangle2(2, 2, 2))

    def test_isosceles_triangles_have_exactly_two_sides_equal(self):
        self.assertEqual('isosceles', triangle2(3, 4, 4))

    def test_scalene_triangles_have_no_equal_sides(self):
        self.assertEqual('scalene', triangle2(3, 4, 5))
