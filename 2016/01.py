#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
adventofcode.com - day 01
"""

import collections
import enum


class Direction(enum.Enum):
    north = 0
    east = 1
    south = 2
    west = 3


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = Direction.north

    def turn_right(self):
        if self.direction == Direction.north:
            self.direction = Direction.east
        elif self.direction == Direction.east:
            self.direction = Direction.south
        elif self.direction == Direction.south:
            self.direction = Direction.west
        elif self.direction == Direction.west:
            self.directon = Direction.north

    def turn_left(self):
        if self.direction == Direction.north:
            self.direction = Direction.west
        elif self.direction == Direction.west:
            self.direction = Direction.south
        elif self.direction == Direction.south:
            self.direction = Direction.east
        elif self.direction == Direction.east:
            self.directon = Direction.north

    def move_forward(self, num_blocks):
        if self.direction == Direction.north:
            self.y += num_blocks
        elif self.direction == Direction.east:
            self.x += num_blocks
        elif self.direction == Direction.south:
            self.y -= num_blocks
        elif self.direction == Direction.west:
            self.x -= num_blocks
        else:
            raise ValueError('invalid direction: %s' % self.direction)

    def __str__(self):
        return '({x}, {y}) / {direction}'.format(x=self.x, y=self.y, direction=self.direction)


if __name__ == '__main__':
    with open('01.txt') as infile:
        content = infile.readline()

    instructions = content.strip('\n').split(',')

    position = Position()

    for instr in instructions:
        instr = instr.strip(' ')
        print('handling "%s"' % instr)
        direction = instr[0]

        try:
            distance = int(instr[1:])
        except ValueError as err:
            raise ValueError('invalid input: %s' % instr) from err

        if direction == 'R':
            position.turn_right()
        elif direction == 'L':
            position.turn_left()
        else:
            raise ValueError('invalid input: %s' % direction)

        position.move_forward(distance)

    print(abs(0 - position.x) + abs(0 - position.y))
