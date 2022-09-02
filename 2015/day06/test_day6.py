from day6 import Light, Instruction, make_grid, execute, total_brightness

import pytest


def test_turn_off_light():
    light = Light(state=1)
    light = light.turn_off()
    assert not light.is_on()
    assert light.brightness == 0


def test_turn_on_light():
    light = Light(state=0)
    light = light.turn_on()
    assert light.is_on()
    assert light.brightness == 1


def test_toggle_light():
    light = Light(state=0)
    light = light.toggle()
    assert light.is_on()
    assert light.brightness == 2
    light = light.toggle()
    assert not light.is_on()
    assert light.brightness == 4


@pytest.mark.parametrize(
    "text,expected_instruction",
    [
        (
            "toggle 461,550 through 564,900\n",
            Instruction(
                operation="toggle",
                start=(461, 550),
                end=(564, 900),
            ),
        ),
        (
            "turn on 461,550 through 564,900\n",
            Instruction(
                operation="turn on",
                start=(461, 550),
                end=(564, 900),
            ),
        ),
        (
            "turn off 461,550 through 564,900\n",
            Instruction(
                operation="turn off",
                start=(461, 550),
                end=(564, 900),
            ),
        ),
    ],
)
def test_construct_instruction_from_text(text, expected_instruction):
    instruction = Instruction.from_text(text)
    assert instruction == expected_instruction


def test_turn_on_all_lights():
    grid = make_grid()
    raw_instruction = "turn on 0,0 through 999,999"
    instruction = Instruction.from_text(raw_instruction)

    execute(instruction, grid)

    for y, col in enumerate(grid):
        for x, light in enumerate(col):
            assert light.is_on(), f"light at ({x}, {y}) is not on"

    assert total_brightness(grid) == 1000000


def test_toggle_all_light():
    grid = make_grid()
    raw_instruction = "toggle 0,0 through 999,999"
    instruction = Instruction.from_text(raw_instruction)

    execute(instruction, grid)

    assert total_brightness(grid) == 2000000


def test_turn_on_single_light():
    grid = make_grid()
    raw_instruction = "turn on 0,0 through 0,0"
    instruction = Instruction.from_text(raw_instruction)

    execute(instruction, grid)

    assert total_brightness(grid) == 1


def test_toggle_first_line():
    grid = make_grid()
    raw_instruction = "toggle 0,0 through 999,0"
    instruction = Instruction.from_text(raw_instruction)

    execute(instruction, grid)

    y = 0
    for x, light in enumerate(grid[y]):
        assert light.is_on(), f"light at ({x}, {y}) is not on"


def test_toggle_rectangle():
    grid = make_grid()
    instructions = [
        Instruction.from_text("turn on 0,0 through 999,999"),
        Instruction.from_text("turn off 499,499 through 500,500"),
    ]
    for instruction in instructions:
        execute(instruction, grid)

    lights = [
        grid[499][499],
        grid[499][500],
        grid[500][499],
        grid[500][500],
    ]

    assert not any(light.is_on() for light in lights), lights
