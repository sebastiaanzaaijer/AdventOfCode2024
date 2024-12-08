


def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines()
    nx = len(lines[0])
    ny = len(lines)
    total = 0
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            if lines[j][i] == "A": #centre of MAX
                if ((lines[j-1][i-1] == "M" and lines[j+1][i+1] == "S" or lines[j-1][i-1] == "S" and lines[j+1][i+1] == "M") and 
                   (lines[j+1][i-1] == "M" and lines[j-1][i+1] == "S" or lines[j+1][i-1] == "S" and lines[j-1][i+1] == "M")):
                   total += 1
    return total

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))