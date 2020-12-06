import pprint
import argparse
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default="1", choices=("1", "2"))
    return parser.parse_args()


class Grid:
    def __init__(self, grid):
        self.x = 0
        self.y = 0
        self.grid = grid
        self.width = len(lines[0])
        self.height = len(lines)

    def step(self, slope):
        for instruction, n in slope:
            instruction(n=n)

    def right(self, n=1): self.x = (self.x + n) % self.width

    def down(self, n=1):
        self.y += n

    def is_tree(self):
        try:
            return self.grid[self.y][self.x] == "#"
        except IndexError:
            return False

    def reset(self):
        self.x = 0
        self.y = 0


def run(grid, slope):
    steps = 0
    trees = 0
    while steps < grid.height - 1:
        grid.step(slope)
        steps += 1
        if grid.is_tree():
            trees += 1

    return trees


if __name__ == '__main__':
    args = parse_args()

    lines = [line.strip('\n') for line in sys.stdin.readlines()]
    grid = Grid(lines)

    slopes = [
        [(grid.right, 1), (grid.down, 1)],
        [(grid.right, 3), (grid.down, 1)],
        [(grid.right, 5), (grid.down, 1)],
        [(grid.right, 7), (grid.down, 1)],
        [(grid.right, 1), (grid.down, 2)],
        ]
    result = 1
    for i, slope in enumerate(slopes):
        print(i)
        grid.reset()
        try:
            result *= run(grid, slope)
            print(result)
        except IndexError:
            print(grid.x, grid.y)


    print(result)
