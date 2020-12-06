import argparse
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default="1", choices=("1", "2"))
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    pattern = re.compile(r"(?P<ocur_min>\d+)-(?P<ocur_max>\d+)\s(?P<letter>\w):\s(?P<password>\w+)")

    lines = [line for line in sys.stdin.readlines()]

    valid_passwords = []
    for line in lines:
        match = pattern.match(line)
        ocur_min = int(match.group('ocur_min'))
        ocur_max = int(match.group('ocur_max'))
        letter = match.group('letter')
        password = match.group('password')
        
        if args.part == "1":
            num_occurrences = len(re.findall(letter, password))
            if num_occurrences in range(ocur_min, ocur_max + 1):
                valid_passwords.append(password)

        elif args.part == "2":
            letters_to_check = []
            letters_to_check = (password[ocur_min - 1], password[ocur_max - 1])

            if letter == letters_to_check[0] and letter == letters_to_check[1]:
                continue

            if letter in letters_to_check:
                valid_passwords.append(password)


    print(len(valid_passwords))
