from collections import Counter


def solve_puzzle(puzzle_input):
    location_list1, location_list2 = list(
        zip(*(map(int, _.split()) for _ in puzzle_input.splitlines()))
    )
    occurances = Counter(location_list2)
    return sum(item * occurances.get(item, 0) for item in location_list1)


if __name__ == "__main__":
    import os
    import pathlib

    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
