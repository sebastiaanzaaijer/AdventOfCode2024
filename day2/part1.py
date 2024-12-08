from itertools import pairwise

def is_safe(report):
    diff = [b-a for a,b in pairwise(report)]
    return all(0<_<4 for _ in diff) or all(0<-_<4 for _ in diff)


def solve_puzzle(puzzle_input):
    reports = [list(map(int,_.split())) for _ in puzzle_input.splitlines()]
    return sum([is_safe(_) for _ in reports])

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))