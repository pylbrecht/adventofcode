#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
adventofcode.com - day 01
"""


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # 0=north, 1=east, 2=south, 3=west
        self.direction = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def move(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])

        self.turn(direction)
        self.forward(distance)

        return self

    def turn(self, value):
        if value == 'L':
            self.direction = (self.direction - 1) % 4
        elif value == 'R':
            self.direction = (self.direction + 1) % 4
        else:
            raise ValueError('value must be "L" or "R"')

    def forward(self, blocks):
        if self.direction == 0:
            self.y += blocks
        elif self.direction == 1:
            self.x += blocks
        elif self.direction == 2:
            self.y -= blocks
        elif self.direction == 3:
            self.x -= blocks


def get_taxicab_distance(instructions):
    position = Position(0, 0)

    for instr in instructions:
        instr = instr.strip()
        position.move(instr)

    return abs(0 - position.x) + abs(0 - position.y)


if __name__ == '__main__':
    with open('01.txt') as infile:
        content = infile.readline()

    instructions = content.strip('\n').split(',')

    distance = get_taxicab_distance(instructions)

    print(distance)
