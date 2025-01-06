from algorithms.full_solve import *
from algorithms.window_solve import *
from algorithms.inverted_solve import *
from utils import *

'''An example of doing an initial check to try to determine which solver to use.'''

# Check to see if we have more - values than +
def check_optimal(grid:list):
    neg = 0
    size = len(grid) * len(grid[0])
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if neg >= size/2: 
                print("using window solver")
                return True
            if col < 0: neg += 1


if __name__ == "__main__":
    # get parameters for BIG grid
    N, grid = get_example_params(10)
    flag = False

    flag = check_optimal(grid)
    # Run the solver
    if flag:
        elapsed, neighbors = window_solve(grid, N)
        new_arr = modify_grid(grid, neighbors)
        show_results(window_solve, elapsed, neighbors, new_arr, N)
    else:
        elapsed, neighbors = inverted_solve(grid, N)
        new_arr = modify_grid(grid, neighbors)
        show_results(inverted_solve, elapsed, neighbors, new_arr, N)
