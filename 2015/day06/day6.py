import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Light:
    state: int = 0
    brightness: int = 0

    def is_on(self):
        return self.state == 1

    def turn_on(self):
        return Light(state=1, brightness=self.brightness + 1)

    def turn_off(self):
        return Light(state=0, brightness=max(0, self.brightness - 1))

    def toggle(self):
        if self.is_on():
            return Light(state=0, brightness=self.brightness + 2)
        return Light(state=1, brightness=self.brightness + 2)


def make_grid():
    grid = []
    for _ in range(1000):
        grid.append([Light() for _ in range(1000)])
    return grid


@dataclass(frozen=True)
class Instruction:
    operation: str
    start: tuple[int, int]
    end: tuple[int, int]

    @classmethod
    def from_text(cls, text):
        pattern = r"(?P<operation>toggle|turn off|turn on) (?P<start>\d+,\d+) through (?P<end>\d+,\d+)"  # noqa: E501
        match = re.match(pattern, text.strip())
        if not match:
            raise RuntimeError(f"cannot parse instruction: {text}")

        operation = match.group("operation")
        x, y = match.group("start").split(",")
        start = int(x), int(y)
        x, y = match.group("end").split(",")
        end = int(x), int(y)

        return cls(
            operation=operation,
            start=start,
            end=end,
        )


def execute(instruction, grid):
    start_x, start_y = instruction.start
    end_x, end_y = instruction.end

    for y, row in enumerate(grid[start_y : end_y + 1]):
        for x, light in enumerate(row[start_x : end_x + 1]):
            if instruction.operation == "turn on":
                grid[start_y + y][start_x + x] = light.turn_on()
            elif instruction.operation == "turn off":
                grid[start_y + y][start_x + x] = light.turn_off()
            elif instruction.operation == "toggle":
                grid[start_y + y][start_x + x] = light.toggle()
            else:
                raise ValueError(f"unknown operation: {instruction.operation}")


def total_brightness(grid):
    total_brightness = 0
    for col in grid:
        for light in col:
            total_brightness += light.brightness

    return total_brightness


if __name__ == "__main__":
    instructions = [
        Instruction.from_text(line.strip())
        for line in sys.stdin.read().split("\n")
        if line
    ]
    grid = make_grid()
    for instruction in instructions:
        execute(instruction, grid)

    count = 0
    for y, col in enumerate(grid):
        for x, light in enumerate(col):
            if light.is_on():
                count += 1

    print(count)
    print(total_brightness(grid))
