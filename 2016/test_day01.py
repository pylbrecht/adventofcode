#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from day01 import get_taxicab_distance


@pytest.mark.parametrize(
    ('instructions', 'distance'),
    [
        (['R2', 'L3'], 5),
        (['R2', 'R2', 'R2'], 2),
        (['R5', 'L5', 'R5', 'R3'], 12),
    ]
)
def test_get_taxicab_geometry(instructions, distance):
    assert get_taxicab_distance(instructions) == distance
