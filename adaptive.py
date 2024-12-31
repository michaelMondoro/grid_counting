from full_solve import *
from window_solve import *
from inverted_solve import *
from utils import *

N, grid = get_example_params(10)


flag = False

def check_optimal(grid):
    neg = 0
    size = len(grid) * len(grid[0])
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if neg >= size/2: 
                print("using window solver")
                return True
            if col < 0: neg += 1

flag = check_optimal(grid)
# Run the solver
print(f"ok {flag}")
if flag:
    elapsed, neighbors = window_solve(grid, N)
else:
    elapsed, neighbors = inverted_solve(grid, N)

# Modify our grid with 0s for display
new_arr = modify_grid(grid, neighbors)

# Display results
print(f"{len(neighbors)} neighbors")
print(f"time: {round(elapsed,5)}s")