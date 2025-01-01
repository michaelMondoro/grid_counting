import sys
from algorithms.full_solve import *
from algorithms.window_solve import *
from algorithms.inverted_solve import *
from utils import *

if __name__ == "__main__":
    if len(sys.argv) > 1: 
        solver = sys.argv[1]
        example = 1 if len(sys.argv) < 3 else int(sys.argv[2])
    else:
        print("usage:\n python main.py [full | window | inverted | compare] [1-10]")
        exit()

    # Get data values for our example
    N, grid = get_example_params(example)
    if solver == "full":
        elapsed, neighbors = full_solve(grid, N)
        new_arr = modify_grid(grid, neighbors)
        show_results(full_solve, elapsed, neighbors, new_arr, N)

    elif solver == "window":
        elapsed, neighbors = window_solve(grid, N)
        new_arr = modify_grid(grid, neighbors)
        show_results(window_solve, elapsed, neighbors, new_arr, N)

    elif solver == "inverted":
        elapsed, neighbors = inverted_solve(grid, N)
        new_arr = modify_grid(grid, neighbors)
        show_results(inverted_solve, elapsed, neighbors, new_arr, N)

    elif solver == "compare":
        for solve in [full_solve, window_solve, inverted_solve]:
            elapsed, neighbors = solve(grid, N)
            new_arr = modify_grid(grid, neighbors)
            show_results(solve, elapsed, neighbors, new_arr, N)
    else:
        print("valid solvers: [ full, window, inverted, compare ]")
        exit()
    

    if (example < 10):
        show_plot(new_arr, example, neighbors, round(elapsed,5))