import pytest

from day7 import Program


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
