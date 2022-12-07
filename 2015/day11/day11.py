def has_increasing_straight(password: str) -> bool:
    raise NotImplementedError


def has_confusing_letters(password: str) -> bool:
    confusing_letters = "iol"
    return any(letter in password for letter in confusing_letters)


def increment_password(password: str) -> str:
    next_char, carry = increment_char(password[-1], False)

    if carry:
        return increment_password(password[:-1]) + next_char

    return password[:-1] + next_char


def increment_char(char: str, carry: bool) -> tuple[str, bool]:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = alphabet.find(char)
    increment = 2 if carry else 1
    carry = char == "z"
    return alphabet[(index + increment) % len(alphabet)], carry
