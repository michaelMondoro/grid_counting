import sys
import matplotlib.pyplot as plt
from full_solve import *
from window_solve import *
from inverted_solve import *
from utils import *

if __name__ == "__main__":
    if len(sys.argv) > 1: 
        solver = sys.argv[1]
        example = 1 if len(sys.argv) < 3 else int(sys.argv[2])
    else:
        print("usage:\n python main.py [full | window | inverted | compare] [1-10]")
        exit()

    if solver == "full":
        solvers = [("full", full_solve)]
    elif solver == "window":
        solvers = [("window", window_solve)]
    elif solver == "inverted":
        solvers = [("inverted", inverted_solve)]
    elif solver == "compare":
        solvers = [("full", full_solve), ("window", window_solve), ("inverted", inverted_solve)]
    else:
        print("valid solvers: [ full, window, inverted, compare ]")
        exit()
   
    # Get data values for our example
    N, grid = get_example_params(example)
    for solve in solvers:
        # Run the solver
        elapsed, neighbors = solve[1](grid, N)
        # Modify our grid with 0s for display
        new_arr = modify_grid(grid, neighbors)

        # Display results
        print(f"\nSolver: {solve[0]} \nN={N}")
        print(f"{len(neighbors)} neighbors")
        print(f"time: {round(elapsed,5)}s")
    
    print(new_arr)

    if (example < 10):
        show_plot(new_arr, example, neighbors, round(elapsed,5))