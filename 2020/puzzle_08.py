import copy
import math
import pprint
import sys
from dataclasses import dataclass, field
from typing import List, Iterable


@dataclass
class Instruction:
    name: str
    operator: int
    executed: bool = False

    @classmethod
    def create_from(cls, line: str) -> "Instruction":
        name, operator = line.split(" ")
        return Instruction(name=name, operator=int(operator))

    def __repr__(self):
        return f"{self.name} {self.operator}"


@dataclass
class CPU:
    pc: int = 0
    acc: int = 0
    history: List[Instruction] = field(default_factory=list)

    def execute(self, instruction: Instruction):
        instruction.executed = True
        self.history.append(instruction)

        if instruction.name == "acc":
            self.acc += instruction.operator
            self.pc += 1
        elif instruction.name == "jmp":
            self.pc += instruction.operator
        elif instruction.name == "nop":
            self.pc += 1
        else:
            raise NotImplementedError(
                f"unsupported instruction: {repr(instruction.name)}"
            )

    def run(self, instructions: List[Instruction]):
        while True:
            try:
                instruction = instructions[self.pc]
            except LookupError:
                print(f"Terminated. Accumulator: {self.acc}")
                return 0

            if instruction in self.history:
                print(
                    f"Found infinite loop: {self.history[-1]}. Accumulator: {self.acc}"
                )
                self.reset()
                return -1

            self.execute(instruction)

    def reset(self):
        self.pc = 0
        self.acc = 0
        self.history = []


def mutate_instructions(instructions) -> Iterable[List[Instruction]]:
    swappable_indices = [
        i
        for i, instruction in enumerate(instructions)
        if instruction.name in ("nop", "jmp")
    ]

    for index in swappable_indices:
        swapped_instructions = copy.deepcopy(instructions)
        
        name = swapped_instructions[index].name
        swapped_instructions[index].name = 'nop' if name == 'jmp' else 'jmp'

        yield swapped_instructions


def bruteforce(cpu, instructions):
    mutated_instructions = mutate_instructions(instructions)
    exit_code = -1
    while exit_code != 0:
        exit_code = cpu.run(next(mutated_instructions))


if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    sys.stdin = open("/dev/tty")

    instructions = [Instruction.create_from(line) for line in lines]

    cpu = CPU()

    bruteforce(cpu, instructions)
