from day11 import (
    increment_char,
    increment_password,
    generate_next_password,
    has_increasing_straight,
    has_confusing_letters,
)

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
        ("yzz", "zaa"),
    ],
)
def test_increment_password(password, next_password):
    assert increment_password(password) == next_password


@pytest.mark.parametrize(
    "password,next_password",
    [
        ("abcdefgh", "abcdffaa"),
        ("ghijklmn", "ghjaabcc"),
    ],
)
def test_next_password(password, next_password):
    assert generate_next_password(password) == next_password


@pytest.mark.parametrize(
    "char,next_char,carry_in,carry_out",
    [
        ("x", "y", False, False),
        ("y", "z", False, False),
        ("z", "a", False, True),
        ("a", "c", True, False),
    ],
)
def test_increment_character(char, next_char, carry_in, carry_out):
    assert increment_char(char, carry_in) == (next_char, carry_out)
