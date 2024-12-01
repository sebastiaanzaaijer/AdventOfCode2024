def solve_puzzle(puzzle_input):
    location_list1, location_list2 = list(zip(*(map(int,_.split()) for _ in puzzle_input.splitlines())))
    return sum(abs(i1-i2) for i1,i2 in zip(sorted(location_list1),sorted(location_list2)))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))