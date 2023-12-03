"""AoC 3, 2023 - Gear Ratios"""

import pathlib
import re
import string
import sys
from dataclasses import dataclass

SYMBOLS = set(string.punctuation) - {"."}


@dataclass
class Symbol:
    x: int
    y: int
    symbol: str

    @property
    def is_gear(self) -> bool:
        return self.symbol == "*"


@dataclass
class Number:
    x: int
    y: int
    number: int
    len: int

    def adjacent_symbol(self, symbol: Symbol) -> bool:
        return (
            self.x - 1 <= symbol.x <= self.x + self.len
            and self.y - 1 <= symbol.y <= self.y + 1
        )


def parse_symbols(data: list[str]) -> list[Symbol]:
    symbols = []
    for y, line in enumerate(data):
        for x, s in enumerate(line):
            if s in SYMBOLS:
                symbols.append(Symbol(x=x, y=y, symbol=s))

    return symbols


def parse_numbers(data: list[str]) -> list[Number]:
    numbers = []
    for y, line in enumerate(data):
        for m in re.finditer(r"(\d+)", line):
            numbers.append(
                Number(x=m.start(), y=y, number=int(m[1]), len=m.end() - m.start())
            )

    return numbers


def part1(symbols: list[Symbol], numbers: list[Number]) -> int:
    parts = []
    for number in numbers:
        for symbol in symbols:
            if number.adjacent_symbol(symbol):
                parts.append(number.number)
                break

    return sum(parts)


def part2(symbols: list[Symbol], numbers: list[Number]) -> int:
    gears = []
    for symbol in symbols:
        if not symbol.is_gear:
            continue
        parts = [number.number for number in numbers if number.adjacent_symbol(symbol)]
        if len(parts) == 2:
            gears.append(parts[0] * parts[1])

    return sum(gears)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        with pathlib.Path(path).open() as f:
            data = f.readlines()
            symbols = parse_symbols(data)
            numbers = parse_numbers(data)
            print("Part 1:", part1(symbols, numbers))
            print("Part 2:", part2(symbols, numbers))
