import enum
from dataclasses import dataclass
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Seat:
    class State(enum.Enum):
        OCCUPIED = 1
        EMPTY = 2
        FLOOR = 3

        @classmethod
        def from_str(cls, c: str) -> "State":
            match c:
                case "L":
                    return cls.EMPTY
                case "#":
                    return cls.OCCUPIED
                case ".":
                    return cls.FLOOR
                case _:
                    raise ValueError(f"unknown char: {c}")

    def __init__(self, position: Point, state: State):
        self.position = position
        self.state = state

    def __eq__(self, other: "Seat") -> bool:
        return self.position == other.position and self.state == other.state


def parse_input(data: str) -> list[Seat]:
    layout = []
    for y, row in enumerate(data.split("\n")):
        for x, c in enumerate(row):
            seat = Seat(position=Point(x, y), state=Seat.State.from_str(c))
            layout.append(seat)
    return layout


if __name__ == "__main__":
    pass
