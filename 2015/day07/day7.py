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
