#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code - Day 3
======================

Perfectly Spherical Houses in a Vacuum
"""

__author__ = "pylbrecht"
__contact__ = "pylbrecht@gmail.com"


import collections
import sys


class Cursor:
    """
    Cursor to move over a 2-dimensional grid.
    """
    def __init__(self, x=0, y=0):
        """
        Initialize coordinates. (default: 0)
        """
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        """
        Return coordinates as a tuple.
        """
        return self.x, self.y

    def move(self, direction):
        """
        Move one step into a specific direction (north/south/east/west).
        """
        if direction == '^':
            self.go_north()

        elif direction == '>':
            self.go_east()

        elif direction == 'v':
            self.go_south()

        elif direction == '<':
            self.go_west()

    def go_north(self):
        """
        Move one step north.
        """
        self.y += 1

    def go_east(self):
        """
        Move on step east.
        """
        self.x += 1

    def go_south(self):
        """
        Move one step south.
        """
        self.y -= 1

    def go_west(self):
        """
        Mone one step west.
        """
        self.x -= 1


class Grid:
    """
    Representation of a 2D grid of houses.

    Map coordinates to number of visits using collections.defaultdict(int).
    """
    def __init__(self):
        """
        Constructor
        """
        self.grid = collections.defaultdict(int)

    def visit(self, coordinates):
        """
        Visit a cell specified by coordinates.
        """
        self.grid[coordinates] += 1

    def cells(self):
        """
        Iterator over all cells.

        Yields (coordinates, number of visits) as key-value pair.
        """
        for key, val in self.grid.items():
            yield key, val


if __name__ == "__main__":
    directions = sys.stdin.read()

    grid = Grid()
    cursor = Cursor()

    for direction in directions:
        grid.visit(cursor.coordinates)
        cursor.move(direction)

    total = 0
    for _, visits in grid.cells():
        if visits > 0:
            total += 1

    print("Santa on his own: %d" % total)

    #####################################################################

    grid = Grid()

    cursor_robot = Cursor()
    cursor_santa = Cursor()

    for direction in directions[0::2]:
        grid.visit(cursor_robot.coordinates)
        cursor_robot.move(direction)

    for direction in directions[1::2]:
        grid.visit(cursor_santa.coordinates)
        cursor_santa.move(direction)

    total = 0
    for _, visits in grid.cells():
        if visits > 0:
            total += 1

    print("Santa with his little robo-helper: %d" % total)
