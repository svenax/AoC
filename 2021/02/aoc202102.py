"""AoC 2, 2021"""

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [(z[0], int(z[1])) for x in puzzle_input.splitlines() if (z := x.split())]


def part1(data):
    """Solve part 1"""
    x, y = 0, 0
    for t, d in data:
        if t == "down":
            y += d
        elif t == "forward":
            x += d
        elif t == "up":
            y -= d
    return x * y


def part2(data):
    """Solve part 2"""
    x, y, aim = 0, 0, 0
    for t, d in data:
        if t == "down":
            aim += d
        elif t == "forward":
            x += d
            y += aim * d
        elif t == "up":
            aim -= d
    return x * y


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
