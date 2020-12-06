from puzzle_05 import *

import pytest


@pytest.mark.parametrize(
        "code,row,column,seat_id",
        [
            ('FBFBBFFRLR', 44, 5, 357),
            ('BFFFBBFRRR', 70, 7,  567),
            ('FFFBBBFRRR', 14, 7,  119),
            ('BBFFBBFRLL', 102, 4,  820),
            ]
        )
def test_find_seat(code, row, column, seat_id):
    seat = Seat.create_from(code)
    assert seat.row == row
    assert seat.column == column
    assert seat.id == seat_id
