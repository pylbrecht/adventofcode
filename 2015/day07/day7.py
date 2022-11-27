from dataclasses import dataclass


class Program:
    def run(self, code):
        raise NotImplementedError


IntegerLiteral = int
Identifier = str
Operand = IntegerLiteral | Identifier


@dataclass
class BitwiseOperation:
    op: str
    right: Operand
    left: Operand | None


def parse_expression(expr):
    if expr.isdigit():
        return int(expr)

    tokens = expr.split(" ")

    try:
        left, op, right = tokens
    except ValueError:
        left, op, right = [None, *tokens]

    if left and left.isdigit():
        left = int(left)
    if right.isdigit():
        right = int(right)

    return BitwiseOperation(left=left, op=op, right=right)
