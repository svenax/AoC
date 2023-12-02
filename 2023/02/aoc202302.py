"""AoC 2, 2023 - Cube Conundrum"""

import pathlib
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class CubeSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    @property
    def power(self) -> int:
        return self.red * self.green * self.blue

    def __le__(self, other: Self) -> bool:
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )


def parse(data: list[str]) -> dict[int, list[CubeSet]]:
    def parse_game(game: str) -> CubeSet:
        cubes = CubeSet()
        for rgb in game.split(", "):
            match rgb.split():
                case [x, ("red" | "green" | "blue") as color]:
                    cubes.__setattr__(color, int(x))

        return cubes

    games = {}
    for game in data:
        game_name, game_data = game.split(": ")
        game_number = int(game_name.removeprefix("Game "))
        games[game_number] = [parse_game(g) for g in game_data.split("; ")]

    return games


def reduce(data: dict[int, list[CubeSet]]) -> dict[int, CubeSet]:
    game_min = {}
    for game_number, games in data.items():
        game_min[game_number] = CubeSet(
            red=max(g.red for g in games),
            green=max(g.green for g in games),
            blue=max(g.blue for g in games),
        )

    return game_min


def part1(data: dict[int, CubeSet], max_cubes: CubeSet) -> int:
    game_sum = 0
    for game_number, game_min in data.items():
        if game_min <= max_cubes:
            game_sum += game_number

    return game_sum


def part2(data: dict[int, CubeSet]) -> int:
    return sum(g.power for g in data.values())


ELF_CUBES = CubeSet(red=12, green=13, blue=14)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        with pathlib.Path(path).open() as f:
            data = reduce(parse(f.readlines()))
            print("Part 1:", part1(data, ELF_CUBES))
            print("Part 2:", part2(data))
