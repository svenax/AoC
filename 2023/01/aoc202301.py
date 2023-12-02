"""AoC 1, 2023 - Trebuchet?!"""

import pathlib
import sys

import regex

NUMBER_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def find_number(item: str, *, from_end: bool = False, include_words: bool = False) -> str:
    pattern = "1|2|3|4|5|6|7|8|9"
    pattern += "|" + "|".join(NUMBER_WORDS.keys()) if include_words else ""
    reverse = "(?r)" if from_end else ""
    res = regex.search(f"{reverse}({pattern})", item)
    match = res.group(1) if res else "0"

    if include_words:
        if match in NUMBER_WORDS:
            return NUMBER_WORDS[match]
    return match

def part1(data: list[str]):
    numbers = [
        int(f"{find_number(i)}{find_number(i, from_end=True)}")
        for i in data
    ]

    return sum(numbers)

def part2(data: list[str]):
    numbers = [
        int(f"{find_number(i, include_words=True)}{find_number(i, from_end=True, include_words=True)}")
        for i in data
    ]

    return sum(numbers)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        with pathlib.Path(path).open() as f:
            data = f.readlines()
            print("Part 1:", part1(data))
            print("Part 2:", part2(data))
