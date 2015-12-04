#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code
==============

Day 1 - Not Quite Lisp
"""

__author__ = "pylbrecht"
__contact__ = "pylbrecht@gmail.com"


import sys


class Santa:
    """
    Representation of Santa delivering presents in a large appartment building.
    """
    def __init__(self, floor=0):
        """
        Initialize floor (default: 0).
        """
        self.floor = floor

    def move(self, instruction):
        """
        Move to the specified instruction.
        """
        if instruction == "(":
            self.floor += 1
        elif instruction == ")":
            self.floor -= 1
        else:
            raise Exception("invalid input: %s" % instruction)


if __name__ == "__main__":
    instructions = sys.stdin.read()
    santa = Santa()

    entered_basement = False

    for index, step in enumerate(instructions):
        santa.move(step)

        if not entered_basement and santa.floor == -1:
            basement = index + 1
            entered_basement = True

    print("final floor: %d" % santa.floor)
    print("entered basement at position: %d" % basement)
