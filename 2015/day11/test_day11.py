from day11 import increment_password, has_increasing_straight, has_confusing_letters

import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        ("hijklmmn", True),
        ("abbceffg", False),
    ],
)
def test_has_increasing_straight(password, result):
    assert has_increasing_straight(password) is result


@pytest.mark.parametrize(
    "password,result",
    [
        ("abc", False),
        ("abci", True),
        ("abco", True),
        ("abcl", True),
    ],
)
def test_has_confusing_letters(password, result):
    assert has_confusing_letters(password) is result


@pytest.mark.parametrize(
    "password,next_password",
    [
        ("xx", "xy"),
        ("xy", "xz"),
        ("xz", "ya"),
        ("ya", "yb"),
    ],
)
def test_increment_password(password, next_password):
    assert increment_password(password) == next_password
