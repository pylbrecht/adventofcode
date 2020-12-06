import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default="1", choices=("1", "2"))
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    numbers = [int(line) for line in sys.stdin.readlines()]
    result = None

    for i in numbers:
        for j in numbers[i:]:
            if i + j != 2020:
                continue
            result = i * j

            if args.part == "2":
                for k in numbers:
                    if i + j + k != 2020:
                        continue

                    result *= k

    print(result)
