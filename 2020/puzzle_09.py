import sys
from typing import List



def is_valid(number: int, preamble: List[int]) -> bool:
    for i in preamble:
        for j in preamble:
            if i == j:
                continue

            if i + j == number:
                return True

    return False


def attack(cipher: List[int], len_preamble: int = 25) -> bool:
    for i, number in enumerate(cipher[len_preamble:]):
        preamble = cipher[i:len_preamble + i]
        if is_valid(number, preamble):
            continue

        return number


def find_contiguous_set(cipher: List[int], key: int) -> List[int]:
    set_ = []
    for start, _ in enumerate(cipher):
        set_.append(cipher[start])
        end = start + 1
        while sum(set_) < key:
            set_.append(cipher[end])
            end += 1

        if sum(set_) > key:
            set_.clear()
            continue

        return set_

    raise RuntimeError("oops")


if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin.readlines()]
    sys.stdin = open('/dev/tty')

    cipher = [int(number) for number in lines]
    key = attack(cipher)

    print(key)

    contiguous_set = find_contiguous_set(cipher, key=key)

    weakness = min(contiguous_set) + max(contiguous_set)
    print(weakness)
