#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code Tests
====================

Day 2 - I Was Told There Would Be No Math

"""

import pytest

from day2 import *


@pytest.fixture
def present():
    """
    A test present.
    """
    return Present(2, 3, 4)


class TestPresent:
    """
    Test the Present() class.
    """
    def test_constructor(self):
        """
        Ensure that the present's dimensions are initialized.
        """
        present = Present(2, 3, 4)

        assert present.length == 2
        assert present.width == 3
        assert present.height == 4

    def test_get_surface(self, present):
        """
        Ensure that the test present's surface is calcualated correctly.
        """
        assert present.surface == 52

    def test_initialize_present_from_string(self):
        """
        Check if the initialization from a dimensions string works.
        """
        dimensions = "2x3x4"
        present = Present.from_string(dimensions)

        assert isinstance(present, Present)
        assert present.length == 2
        assert present.width == 3
        assert present.height == 4

    def test_get_volume(self, present):
        """
        Ensure that the test present's volume is calculated correctly.
        """
        assert present.volume == 24


@pytest.mark.parametrize("present,area", [
    (Present(4, 2, 3), 6),
    (Present(1, 10, 1), 1),
    ])
def test_get_area_of_smallest_side(present, area):
    """
    """
    assert get_area_of_smallest_side(present) == area


@pytest.mark.parametrize("present,distance", [
    (Present(4, 2, 3), 10),
    (Present(1, 10, 1), 4),
    ])
def test_get_shortest_distance_around_sides(present, distance):
    """
    """
    assert get_shortest_distance_around_sides(present) == distance


@pytest.mark.parametrize("present,amount", [
    (Present(2, 3, 4), 58),
    (Present(1, 1, 10), 43),
    ])
def test_amount_of_wrapping_paper_per_present(present, amount):
    """
    """
    assert present.surface + get_area_of_smallest_side(present) == amount


@pytest.mark.parametrize("present,amount", [
    (Present(2, 3, 4), 34),
    (Present(1, 1, 10), 14),
    ])
def test_amount_of_ribbon_per_present(present, amount):
    """
    """
    assert present.volume + get_shortest_distance_around_sides(present) == amount
