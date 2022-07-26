from puzzle_11 import *


def test_parse_input():
    input_ = "L.\nL#\n"
    expected = [
        (Seat(position=Point(0, 0), state=Seat.State.EMPTY)),
        (Seat(position=Point(1, 0), state=Seat.State.FLOOR)),
        (Seat(position=Point(0, 1), state=Seat.State.EMPTY)),
        (Seat(position=Point(1, 1), state=Seat.State.OCCUPIED)),
    ]
    assert parse_input(input_) == expected
