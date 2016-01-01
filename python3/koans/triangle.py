#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle() analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
def triangle(a, b, c):
    unique_sides = set([a, b, c])
    if len(unique_sides) == 1:
        return 'equilateral'
    elif len(unique_sides) == 2:
        return 'isosceles'
    else:
        return 'scalene'


# triangle2() contains the same logic as triangle() expect that it also adds
# some error handling for bad inputs.
#
# The tests for this method can be found in
#   about_triangle_project_2.py
def triangle2(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] <= 0:
        raise TriangleError('Sides cannot be 0 or less')
    if sides[2] >= sides[0] + sides[1]:
        raise TriangleError('Sum of two sides must be greater than the remaining side')
    return triangle(a, b, c)


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
