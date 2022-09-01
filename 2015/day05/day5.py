import sys


RULES = {
    "part1": (
        lambda text: len(vowels(text)) >= 3,
        lambda text: len(repeating_letters(text)) >= 1,
        lambda text: not contains_arbitrary_pairs(text),
    ),
    "part2": (
        lambda text: has_matching_pairs(text),
        lambda text: has_skippy_pair(text),
    ),
}


def vowels(text):
    return [c for c in text if c in "aeiou"]


def repeating_letters(text):
    letters = []
    for i, c in enumerate(text):
        cursor = i + 1
        group = c
        while cursor < len(text) and c == text[cursor]:
            group += text[cursor]
            cursor += 1

        if len(group) > 1:
            letters.append(group)

    return letters


def contains_arbitrary_pairs(text):
    pairs = ("ab", "cd", "pq", "xy")
    return any(pair in text for pair in pairs)


def is_nice(text, rules):
    for rule in rules:
        if not rule(text):
            return False
    return True


def has_matching_pairs(text):
    for i, pair in pairs(text):
        for _, other_pair in pairs(text[i+len(pair):]):
            if pair != other_pair:
                continue
            return True
    return False


def pairs(text):
    """Return pairs of letters in the form o (start index, pair)."""
    cursor = 0
    while cursor < len(text) - 1:
        yield cursor, text[cursor:cursor+2]
        cursor += 1


def has_skippy_pair(text):
    cursor = 0
    while cursor + 2 < len(text):
        if text[cursor] == text[cursor + 2]:
            return True
        cursor += 1
    return False


if __name__ == "__main__":
    strings = [s.strip() for s in sys.stdin.read().split("\n")]

    nice = [s for s in strings if is_nice(s, RULES["part1"])]
    print(f"nice: {len(nice)}")

    nice = [s for s in strings if has_matching_pairs(s) and has_skippy_pair(s)]
    print(f"nice: {len(nice)}")
