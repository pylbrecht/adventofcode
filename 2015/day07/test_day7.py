import pytest

from day7 import evaluate


@pytest.mark.parametrize(
    "wire,result",
    [
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("x", 123),
        ("y", 456),
    ],
    ids=[
        "x AND y",
        "x OR y",
        "x LSHIFT 2",
        "y RSHIFT 2",
        "NOT x",
        "NOT y",
        "123",
        "456",
    ],
)
def test_evaluate(wire, result):
    # TODO: write a function to produce such a dict
    instructions = {
        "d": "x AND y",
        "e": "x OR y",
        "f": "x LSHIFT 2",
        "g": "y RSHIFT 2",
        "h": "NOT x",
        "i": "NOT y",
        "x": "123",
        "y": "456",
    }
    assert evaluate(wire=wire, instructions=instructions, resolved={}) == result
