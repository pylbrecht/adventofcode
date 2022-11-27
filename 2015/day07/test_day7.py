import pytest

from day7 import Program, BitwiseOperation, parse_expression


@pytest.mark.xfail(reason="unimplemented")
def test_example():
    code = (
        "123 -> x\n"
        "456 -> y\n"
        "x AND y -> d\n"
        "x OR y -> e\n"
        "x LSHIFT 2 -> f\n"
        "y RSHIFT 2 -> g\n"
        "NOT x -> h\n"
        "NOT y -> i\n"
    )
    program = Program()
    program.run(code)

    expected_wires = {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }
    assert program.wires == expected_wires


@pytest.mark.parametrize(
    "expr,result",
    [
        ("123", 123),
        ("x AND y", BitwiseOperation(op="AND", left="x", right="y")),
        ("x LSHIFT 2", BitwiseOperation(op="LSHIFT", left="x", right=2)),
        ("NOT y", BitwiseOperation(op="NOT", left=None, right="y")),
    ],
)
def test_parse_expression(expr, result):
    assert parse_expression(expr) == result
