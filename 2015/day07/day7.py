from dataclasses import dataclass


class Program:
    def __init__(self):
        self.wires = {}

    def run(self, code):
        statements = [line.strip() for line in code.split("\n") if line]
        for statement in statements:
            expr, dest = statement.split("->")

            expr = parse_expression(expr.strip())
            dest = dest.strip()

            # eval expression
            if isinstance(expr, int):
                self.wires[dest] = expr
            else:
                # bitwise
                if expr.op == "NOT":
                    try:
                        right = self.wires[expr.right]
                    except LookupError:
                        right = expr.right

                    self.wires[dest] = right ^ 0xFFFF
                else:
                    try:
                        right = self.wires[expr.right]
                    except LookupError:
                        right = expr.right

                    try:
                        left = self.wires[expr.left]
                    except LookupError:
                        left = expr.left

                    if expr.op == "AND":
                        self.wires[dest] = left & right
                    elif expr.op == "OR":
                        self.wires[dest] = left | right
                    elif expr.op == "LSHIFT":
                        self.wires[dest] = left << right
                    elif expr.op == "RSHIFT":
                        self.wires[dest] = left >> right


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
