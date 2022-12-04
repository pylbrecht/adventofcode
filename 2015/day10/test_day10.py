from day10 import look_and_say

import pytest


@pytest.mark.parametrize(
    "looked,said",
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
    ],
)
def test_look_and_say(looked, said):
    assert look_and_say(looked) == said
