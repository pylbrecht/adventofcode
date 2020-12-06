from puzzle_06 import *

import pytest


@pytest.fixture
def puzzle_input():
    return "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"


def test_create_groups(puzzle_input):
    groups = [
        Group(people=[Person(questions="abc")]),
        Group(
            people=[Person(questions="a"), Person(questions="b"), Person(questions="c")]
        ),
        Group(people=[Person(questions="ab"), Person(questions="ac")]),
        Group(
            people=[
                Person(questions="a"),
                Person(questions="a"),
                Person(questions="a"),
                Person(questions="a"),
            ]
        ),
        Group(people=[Person(questions="b")]),
    ]
    assert create_groups(puzzle_input) == groups


@pytest.mark.parametrize(
        "group,count",
        [
            (Group(people=[Person(questions="abc")]), 3),
        (Group(
            people=[Person(questions="a"), Person(questions="b"), Person(questions="c")]
        ), 3),
            (Group(people=[Person(questions="ab"), Person(questions="ac")]), 3),
        (Group(
            people=[
                Person(questions="a"),
                Person(questions="a"),
                Person(questions="a"),
                Person(questions="a"),
            ]
        ), 1),
        (Group(people=[Person(questions="b")]), 1),
            ]
        )
def test_any_yes(group, count):
    assert group.any_yes() == count


@pytest.mark.parametrize(
        "group,count",
        [
            (Group(people=[Person(questions="abc")]), 3),
        (Group(
            people=[Person(questions="a"), Person(questions="b"), Person(questions="c")]
        ), 0),
            (Group(people=[Person(questions="ab"), Person(questions="ac")]), 1),
        (Group(
            people=[
                Person(questions="a"),
                Person(questions="a"),
                Person(questions="a"),
                Person(questions="a"),
            ]
        ), 1),
        (Group(people=[Person(questions="b")]), 1),
            ]
        )
def test_all_yes(group, count):
    assert group.all_yes() == count


def test_total_any_yes(puzzle_input):
    groups = create_groups(puzzle_input)
    assert sum([group.any_yes() for group in groups]) == 11


def test_total_all_yes(puzzle_input):
    groups = create_groups(puzzle_input)
    assert sum([group.all_yes() for group in groups]) == 6
