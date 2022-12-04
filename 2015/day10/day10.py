import sys
import itertools


def look_and_say(input_: str) -> str:
    result = ""

    for key, group in itertools.groupby(input_):
        result += f"{len(list(group))}{key}"

    return result


if __name__ == "__main__":
    [input_] = [line.strip() for line in sys.stdin.read().split("\n") if line]

    part1_input = input_
    for _ in range(40):
        result = look_and_say(part1_input)
        part1_input = result

    print(len(result))

    part2_input = input_
    for _ in range(50):
        result = look_and_say(part2_input)
        part2_input = result

    print(len(result))
