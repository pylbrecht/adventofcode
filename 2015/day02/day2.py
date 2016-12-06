#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code
==============

Day 2 - I Was Told There Would Be No Math

"""

__author__ = "pylbrecht"
__contact__ = "pylbrecht@gmail.com"


import itertools
import re
import sys


class Present:
    """
    Present in form of a box (perfect right rectangular prism).
    """
    def __init__(self, length, width, height):
        """
        Initialize dimensions of the present.
        """
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface(self):
        """
        Surface of the present.
        """
        return 2 * (self.length * self.width +
                    self.width * self.height +
                    self.height * self.length)

    @property
    def volume(self):
        """
        Cubic volume of the present.
        """
        return self.length * self.width * self.height

    @staticmethod
    def from_string(dimensions):
        """
        Construct a Present object from a dimensions string (e.g. "2x3x4").
        """
        pattern = r"^(?P<length>\d+)x(?P<width>\d+)x(?P<height>\d+)$"
        match = re.match(pattern, dimensions)
        if not match:
            raise Exception("invalid dimensions string: %s" % dimensions)

        dimensions = [int(x) for x in match.groups()]
        return Present(*dimensions)

    def __str__(self):
        """
        String representation of a present.
        """
        return "Present({}x{}x{})".format(self.length, self.width, self.height)


def get_area_of_smallest_side(present):
    """
    Return the area of the present's smallest side.
    """
    dimensions = present.length, present.width, present.height
    areas = [a * b for a, b in itertools.combinations(dimensions, 2)]
    return sorted(areas)[0]


def get_shortest_distance_around_sides(present):
    """
    Return the shortest distance around the present's sides.
    """
    dimensions = present.length, present.width, present.height
    a, b = sorted(dimensions)[:2]
    return 2 * (a + b)


if __name__ == "__main__":
    wrapping_paper_total = 0
    ribbon_total = 0

    list_of_dimensions = [x for x in sys.stdin.read().split('\n') if x]

    for dimensions in list_of_dimensions:
        present = Present.from_string(dimensions)

        wrapping_paper = present.surface + get_area_of_smallest_side(present)
        wrapping_paper_total += wrapping_paper

        ribbon = present.volume + get_shortest_distance_around_sides(present)
        ribbon_total += ribbon

    print("total feet of wrapping paper: %d" % wrapping_paper_total)
    print("total feet of ribbon: %d" % ribbon_total)
