import numpy as np 
import matplotlib.pyplot as plt

# Return grid and N value for the given example
def get_example_params(example:int):
    default_arr = np.array([
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    ])
    if example == 1:
        default_arr[5][5] = 1
        N = 3
    elif example == 2:
        default_arr[5][1] = 1
        N = 3
    elif example == 3:
        default_arr[3][7] = 1
        default_arr[7][3] = 1
        N = 2
    elif example == 4:
        default_arr[7][3] = 1
        default_arr[6][5] = 1
        N = 2
    elif example == 5:
        # Multiple + values in corners
        default_arr[0][0] = 1
        default_arr[1][1] = 1
        default_arr[0][1] = 1
        N = 2
    elif example == 6:
        # Even distribution
        default_arr = np.random.choice([-1, 1], size=(11, 11))
        N = 1
    elif example == 7:
        # Side clump
        default_arr[6][9] = 1
        default_arr[5][10] = 1
        default_arr[5][8] = 1
        default_arr[4][9] = 1
        default_arr[4][10] = 1
        N = 2
    elif example == 10:
        # BIG grid example
        default_arr[5][5] = 1
        default_arr =  np.concatenate((default_arr, np.full((1000000, 11), -1)))
        N = 3

    return N, default_arr

def manhattan_dist(a:tuple, b:tuple):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def show_plot(arr, example, neighbors, t):
    plt.imshow(arr, cmap=plt.get_cmap('viridis'))
    plt.colorbar(ticks=[-1, 0, 1])
    plt.title(f"Example {example} | {len(neighbors)} neighbors | {t}sec ")
    plt.show()

def modify_grid(grid, neighbors):
    new_arr = grid.copy()
    for i in neighbors:
        if new_arr[i[0]][i[1]] > 0:
            new_arr[i[0]][i[1]] = 1
        else:
            new_arr[i[0]][i[1]] = 0
    return new_arr