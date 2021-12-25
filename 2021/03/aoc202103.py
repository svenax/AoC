"""AoC 3, 2021"""

import pathlib
import sys

import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return np.transpose([[int(y) for y in list(x)] for x in puzzle_input.splitlines()])


def most_common_bit(arr):
    ones = np.count_nonzero(arr)
    zeros = np.size(arr) - ones

    return 1 if ones > zeros else 0


def bits_to_int(arr):
    return int("".join(str(bit) for bit in arr), base=2)


def part1(data):
    """Solve part 1"""
    gamma = [most_common_bit(row) for row in data]
    epsilon = [0 if most_common_bit(row) else 1 for row in data]

    return bits_to_int(gamma) * bits_to_int(epsilon)


def part2(data):
    """Solve part 2"""
    orig_data = np.transpose(data)
    bits = [most_common_bit(row) for row in data]

    for i, bit in enumerate(bits):
        flt = orig_data[i][orig_data[i] != bit]
        orig_data = np.delete(orig_data, flt, 0)
        print(orig_data)

    # return bits_to_int(oxygen) * bits_to_int(co2)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
