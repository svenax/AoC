"""Tests for AoC 2, 2021"""

import pathlib

import aoc202102
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc202102.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert len(example) == 6
    assert example[0] == ("forward", 5)


def test_part1_example(example):
    """Test part 1 on example input"""
    assert aoc202102.part1(example) == 150


def test_part2_example(example):
    """Test part 2 on example input"""
    assert aoc202102.part2(example) == 900
