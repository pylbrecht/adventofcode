import sys


def encode_string(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def count_chars(text) -> tuple[int, int]:
    return len(text), len(eval(text))


if __name__ == "__main__":
    strings = [s.strip() for s in sys.stdin.read().split("\n") if s]
    total_escaped = 0
    total_memory = 0
    for string_ in strings:
        count_escaped, count_memory = count_chars(string_)
        total_escaped += count_escaped
        total_memory += count_memory

    print(f"{total_escaped} - {total_memory} = {total_escaped - total_memory}")

    total = 0
    for string_ in strings:
        total += len(encode_string(string_)) + 2  # `+ 2` for the enclosing quotes

    print(f"{total} - {total_escaped} = {total - total_escaped}")
