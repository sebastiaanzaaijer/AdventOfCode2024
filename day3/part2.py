from re import compile

pattern = compile(r"(mul\(([\d]{1,3}),([\d]{1,3})\)|don't\(\)|do\(\))")


def solve_puzzle(puzzle_input):
    active = True
    total = 0
    for m in pattern.findall(puzzle_input):
        if m[0] == "do()":
            active = True
            continue
        if m[0] == "don't()":
            active = False
            continue
        if active:
            total += int(m[1]) * int(m[2])
    return total


if __name__ == "__main__":
    import os
    import pathlib

    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
