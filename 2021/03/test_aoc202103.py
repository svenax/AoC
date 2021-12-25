"""Tests for AoC 3, 2021"""

import pathlib

import aoc202103
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc202103.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert len(example) == 5
    assert np.array_equal(example[0], [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0])


def test_part1_example(example):
    """Test part 1 on example input"""
    assert aoc202103.part1(example) == 198


def test_part2_example(example):
    """Test part 2 on example input"""
    assert aoc202103.part2(example) == 230
