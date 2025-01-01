import numpy as np 
import time 
from utils import *

''' 
This solver checks the value of every cell and IF the value is negative, iterates ONLY over the surrounding (N*2)+1)^2 grid 
looking for a single postitive neighbor
'''

def is_neighbor(cur_x:int, cur_y:int, arr:list, N:int):
    WIDTH = len(arr[0])
    HEIGHT = len(arr)
    left_bound = max(cur_x - N, 0)
    right_bound = min(cur_x + N, WIDTH)
    top_bound = max(cur_y - N, 0)
    bottom_bound = min(cur_y + N, HEIGHT)

    window = np.array([row[left_bound:right_bound+1] for row in arr[top_bound:bottom_bound+1]])
    new_x = cur_x - left_bound
    new_y = cur_y - top_bound

    for y, row in enumerate(window):
        for x, col in enumerate(row):
            if (manhattan_dist((new_x, new_y), (x,y)) <= N and col > 0): 
                return True

def inverted_solve(arr:list, N:int):
    start_time = time.perf_counter()
    neighbors = []
    for y,row in enumerate(arr):
        for x,col in enumerate(row):
            if (col > 0): 
                neighbors.append((y,x))
            elif (col < 0 and is_neighbor(x,y, arr, N)):
                neighbors.append((y,x))
    
    end_time = time.perf_counter()
    return (end_time-start_time), set(neighbors)