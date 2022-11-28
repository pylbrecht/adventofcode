import sys


def parse_instructions(input_: str) -> dict[str, str]:
    lines = [line.strip() for line in input_.split("\n") if line]
    instructions = {}
    for line in lines:
        expr, wire = line.split("->")
        instructions[wire.strip()] = expr.strip()

    return instructions


def evaluate(wire: str, instructions: dict[str, str], resolved: dict[str, int]) -> int:
    try:
        return int(wire)
    except ValueError:
        # not an integer literal
        pass

    try:
        return resolved[wire]
    except LookupError:
        pass

    tokens = instructions[wire].split(" ")

    if len(tokens) == 1:
        # found literal
        return evaluate(tokens[0], instructions, resolved)

    op = tokens[-2]

    if op == "NOT":
        resolved[wire] = ~evaluate(tokens[1], instructions, resolved) & 0xFFFF
    elif op == "OR":
        resolved[wire] = evaluate(tokens[0], instructions, resolved) | evaluate(
            tokens[2], instructions, resolved
        )
    elif op == "AND":
        resolved[wire] = evaluate(tokens[0], instructions, resolved) & evaluate(
            tokens[2], instructions, resolved
        )
    elif op == "LSHIFT":
        resolved[wire] = evaluate(tokens[0], instructions, resolved) << evaluate(
            tokens[2], instructions, resolved
        )
    elif op == "RSHIFT":
        resolved[wire] = evaluate(tokens[0], instructions, resolved) >> evaluate(
            tokens[2], instructions, resolved
        )
    else:
        raise ValueError(f"unknown op: {op}")

    return resolved[wire]


if __name__ == "__main__":
    instructions = parse_instructions(sys.stdin.read())
    a = evaluate("a", instructions, {})
    print(a)

    instructions["b"] = f"{a}"
    a = evaluate("a", instructions, {})
    print(a)
