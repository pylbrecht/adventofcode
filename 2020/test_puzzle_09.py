from puzzle_09 import *

import pytest


@pytest.fixture
def cipher():
    return [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]


def test_break_cipher(cipher):
    assert attack(cipher, len_preamble=5) == 127


def test_find_contiguous_set(cipher):
    key = 127
    assert find_contiguous_set(cipher, key) == [15, 25, 47, 40]


@pytest.mark.parametrize(
        "number,result",
        [
            (26, True),
            (49, True),
            (100, False),
            (50, False),
            ]
        )
def test_is_valid_number(number, result):
    preamble = range(1,26)
    assert is_valid(number, preamble) is result
