#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from day1 import *

import pytest


class TestSanta:
    """
    """
    def setup_method(self, method):
        """
        """
        self.santa = Santa()

    def test_constructor(self):
        """
        """
        assert self.santa.floor == 0

    @pytest.mark.parametrize("instructions,floor", [
       ("(())", 0),
       ("()()", 0),
       ("(((", 3),
       ("(()(()(", 3),
       ("))(((((", 3),
       ("())", -1),
       ("))(", -1),
       (")))", -3),
       (")())())", -3),
       ])
    def test_move(self, instructions, floor):
        """
        """
        for step in instructions:
            self.santa.move(step)
        assert self.santa.floor == floor
