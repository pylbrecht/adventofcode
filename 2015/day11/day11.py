def has_increasing_straight(password: str) -> bool:
    raise NotImplementedError


def has_confusing_letters(password: str) -> bool:
    confusing_letters = "iol"
    return any(letter in password for letter in confusing_letters)


def increment_password(password: str) -> str:
    raise NotImplementedError


def increment_char(char: str, carry: bool) -> tuple[str, bool]:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = alphabet.find(char)
    increment = 2 if carry else 1
    carry = char == "z"
    return alphabet[(index + increment) % len(alphabet)], carry
