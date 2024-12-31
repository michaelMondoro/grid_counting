import numpy as np 
import time 
from utils import *

'''
This solver stops on every positive cell and then iterates ONLY over the surrounding (N*2)+1)^2 grid looking for neighbors
'''

def window_search(cur_x:int, cur_y:int, arr:list, N:int):
    WIDTH = len(arr[0])
    HEIGHT = len(arr)
    left_bound = max(cur_x - N, 0)
    right_bound = min(cur_x + N, WIDTH)
    top_bound = max(cur_y - N, 0)
    bottom_bound = min(cur_y + N, HEIGHT)

    window = np.array([row[left_bound:right_bound+1] for row in arr[top_bound:bottom_bound+1]])
    new_x = cur_x - left_bound
    new_y = cur_y - top_bound

    neighbors = []
    for y, row in enumerate(window):
        for x, col in enumerate(row):
            if manhattan_dist((new_x, new_y), (x,y)) <= N: 
                neighbors.append((y+top_bound,x+left_bound)) if ((new_x, new_y)==(x,y)) else neighbors.append((y+top_bound,x+left_bound))
    return neighbors

def window_solve(arr:list, N:int):
    start_time = time.perf_counter()

    neighbors = []
    for y,row in enumerate(arr):
        for x,col in enumerate(row):
            if (col > 0): neighbors += window_search(x,y, arr, N)
    
    end_time = time.perf_counter()
    return (end_time-start_time), set(neighbors)