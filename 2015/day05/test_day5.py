from day5 import (
    vowels,
    repeating_letters,
    is_nice,
    has_matching_pairs,
    has_skippy_pair,
    RULES,
    pairs,
)

import pytest


@pytest.mark.parametrize(
    "text",
    [
        ("aei"),
        ("xazegov"),
        ("aeiouaeiouaeiou"),
    ],
)
def test_at_least_three_vowels(text):
    assert len(vowels(text)) >= 3


@pytest.mark.parametrize(
    "text,letters",
    [
        ("xx", ["xx"]),
        ("dd", ["dd"]),
        ("aabbccdd", ["aa", "bb", "cc", "dd"]),
    ],
)
def test_at_least_one_repeating_letter(text, letters):
    assert repeating_letters(text) == letters
    assert len(repeating_letters(text)) >= 1


@pytest.mark.parametrize(
    "text,rules,result",
    [
        ("ugknbfddgicrmopn", RULES["part1"], True),
        ("aaa", RULES["part1"], True),
        ("jchzalrnumimnmhp", RULES["part1"], False),
        ("haegwjzuvuyypxyu", RULES["part1"], False),
        ("dvszwmarrgswjxmb", RULES["part1"], False),
        ("qjhvhtzxzqqjkmpb", RULES["part2"], True),
        ("xxyxx", RULES["part2"], True),
        ("uurcxstgmygtbstg", RULES["part2"], False),
        ("ieodomkazucvgmuy", RULES["part2"], False),
    ],
)
def test_is_nice(text, rules, result):
    assert is_nice(text, rules) is result


@pytest.mark.parametrize(
    "text,result",
    [
        ("xyxy", True),
        ("aabcdefgaa", True),
        ("abcde", False),
        ("qjhvhtzxzqqjkmpb", True),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_has_matching_pairs(text, result):
    assert has_matching_pairs(text) is result


@pytest.mark.parametrize(
    "text,result",
    [
        ("aaa", True),
        ("xyx", True),
        ("abcdefeghi", True),
        ("abcd", False),
    ],
)
def test_has_skippy_pair(text, result):
    assert has_skippy_pair(text) is result


@pytest.mark.parametrize(
    "text,result",
    [
        ("aabbcc", [(0, "aa"), (1, "ab"), (2, "bb"), (3, "bc"), (4, "cc")]),
    ]
)
def test_pairs(text, result):
    assert list(pairs(text)) == result
