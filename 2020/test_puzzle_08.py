from puzzle_08 import *


def test_instruction_set():
    instructions = [
            Instruction(name='nop', operator=1),
            Instruction(name='acc', operator=3),
            Instruction(name='jmp', operator=3),
            Instruction(name='acc', operator=7),
            ]


    mutated_instructions = [
            [
                Instruction(name='jmp', operator=1),
                Instruction(name='acc', operator=3),
                Instruction(name='jmp', operator=3),
                Instruction(name='acc', operator=7),
                ],
            [
                Instruction(name='nop', operator=1),
                Instruction(name='acc', operator=3),
                Instruction(name='nop', operator=3),
                Instruction(name='acc', operator=7),
                ],
            ]

    assert list(mutate_instructions(instructions)) == mutated_instructions
