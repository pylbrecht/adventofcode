import sys
from typing import Optional, Callable
from dataclasses import dataclass

@dataclass
class Range:
    start: int
    end: int
    last_action: str = None

    def upper(self):
        self.start += round((self.end - self.start) / 2)
        self.last_action = "upper"

    def lower(self):
        self.end -= round((self.end - self.start) / 2)
        self.last_action = "lower"

    @property
    def final(self):
        if self.last_action == "upper":
            return self.end
        return self.start

    def __str__(self):
        return f"({self.start}, {self.end})"


def find_row(code):
    r = Range(0, 127)
    for c in code[:7]:
        if c == "F":
            r.lower()
        elif c == "B":
            r.upper()

    return r.final


def find_column(code):
    r = Range(0, 7)
    for c in code[7:]:
        if c == "L":
            r.lower()
        elif c == "R":
            r.upper()

    return r.final



@dataclass
class Seat:
    row: int
    column: Optional[int] = None

    @property
    def id(self):
        return self.row * 8 + self.column

    @classmethod
    def create_from(cls, code: str):
        row = find_row(code)
        column = find_column(code)
        return cls(row=row, column=column)


if __name__ == '__main__':
    seats = []

    for line in sys.stdin.readlines():
        code = line.strip('\n')

        seats.append(Seat.create_from(code))

    print(max(seat.id for seat in seats))

    seats_available = set(range(46, 992))
    seats_taken = set(seat.id for seat in seats)

    print(seats_available - seats_taken)
