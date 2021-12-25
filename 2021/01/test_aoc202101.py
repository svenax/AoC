"""Tests for AoC 1, 2021"""

import pathlib

import aoc202101
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc202101.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert len(example) == 10
    assert example[0] == 199


def test_part1_example(example):
    """Test part 1 on example input"""
    assert aoc202101.part1(example) == 7


def test_part2_example(example):
    """Test part 2 on example input"""
    assert aoc202101.part2(example) == 5
