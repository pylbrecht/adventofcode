#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
"""

__author__ = "pylbrecht"
__contact__ = "pylbrecht@gmail.com"


import collections
import pytest

from day3 import *


@pytest.fixture
def cursor():
    return Cursor()


class TestCursor:
    """
    """
    def setup_method(self, method):
        """
        """
        self.cursor = Cursor()

    def test_cursor(self):
        """
        """
        assert self.cursor.x == 0
        assert self.cursor.y == 0

    def test_get_coordinates(self):
        """
        """
        assert self.cursor.coordinates == (0, 0)

    def test_go_north(self):
        """
        """
        self.cursor.go_north()
        assert self.cursor.coordinates == (0, 1)

    def test_go_south(self):
        """
        """
        self.cursor.go_south()
        assert self.cursor.coordinates == (0, -1)

    def test_go_east(self):
        """
        """
        self.cursor.go_east()
        assert self.cursor.coordinates == (1, 0)

    def test_go_west(self):
        """
        """
        self.cursor.go_west()
        assert self.cursor.coordinates == (-1, 0)


class TestGrid:
    """
    """
    def setup_method(self, method):
        """
        """
        self.grid = Grid()

    def test_constructor(self):
        """
        """
        assert isinstance(self.grid.grid, collections.defaultdict)


@pytest.mark.parametrize("direction,coordinates", [
    ('^', (0, 1)),
    ('>', (1, 0)),
    ('v', (0, -1)),
    ('<', (-1, 0)),
    ])
def test_move(direction, coordinates, cursor):
    """
    """
    cursor.move(direction)
    assert cursor.coordinates == coordinates
