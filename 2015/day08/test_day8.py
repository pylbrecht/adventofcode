import pytest

from day8 import count_chars, encode_string


@pytest.mark.parametrize(
    "text,count_escaped,count_memory",
    [
        (r'""', 2, 0),
        (r'"abc"', 5, 3),
        (r'"aaa\"aaa"', 10, 7),
        (r'"\x27"', 6, 1),
        (r"\"\"", 6, 0),
    ],
)
def test_count_chars(text, count_escaped, count_memory):
    assert count_chars(text) == (count_escaped, count_memory)


@pytest.mark.parametrize(
    "text,encoded",
    [
        (r'""', r"\"\""),
        (r'"abc"', r"\"abc\""),
        (r'"aaa\"aaa"', r"\"aaa\\\"aaa\""),
        (r'"\x27"', r"\"\\x27\""),
    ],
)
def test_encode_strings(text, encoded):
    assert encode_string(text) == encoded
