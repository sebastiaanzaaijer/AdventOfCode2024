from re import compile

pattern_fwd = compile(r"(XMAS)")
pattern_bck = compile(r"(SAMX)")


def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines()
    nx = len(lines[0])
    ny = len(lines)
    total = 0
    # horizontal
    for line in lines:
        total += len(pattern_fwd.findall(line))
        total += len(pattern_bck.findall(line))
    # vertical
    for column in list(zip(*lines)):
        total += len(pattern_fwd.findall("".join(column)))
        total += len(pattern_bck.findall("".join(column)))
    # diagonal top left to bottom right
    diagonals = zip(*[" " * (nx - i - 1) + l + " " * i for i, l in enumerate(lines)])
    for d in diagonals:
        total += len(pattern_fwd.findall("".join(d).strip()))
        total += len(pattern_bck.findall("".join(d).strip()))
    # diagonal top roght to bottom left
    diagonals = zip(*[" " * i + l + " " * (nx - i - 1) for i, l in enumerate(lines)])
    for d in diagonals:
        total += len(pattern_fwd.findall("".join(d).strip()))
        total += len(pattern_bck.findall("".join(d).strip()))
    return total


if __name__ == "__main__":
    import os
    import pathlib

    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
