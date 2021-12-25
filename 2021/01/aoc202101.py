"""AoC 1, 2021"""

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(x) for x in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1"""
    return sum(data[i] < data[i + 1] for i in range(len(data) - 1))


def part2(data):
    """Solve part 2"""
    depth, prev_depth = 0, 0
    for i in range(len(data) - 2):
        sum = data[i] + data[i + 1] + data[i + 2]
        if prev_depth < sum and prev_depth > 0:
            depth += 1
        prev_depth = sum

    return depth


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
