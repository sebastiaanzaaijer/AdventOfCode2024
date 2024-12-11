from re import compile

pattern = compile(r"(mul\(([\d]{1,3}),([\d]{1,3})\))")


def solve_puzzle(puzzle_input):
    total = 0
    for m in pattern.findall(puzzle_input):
        total += int(m[1]) * int(m[2])
    return total


if __name__ == "__main__":
    import os
    import pathlib

    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
