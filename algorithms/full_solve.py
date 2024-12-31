import time
from utils import *
'''
This solver stops on every positive cell, and then iterates over the entire grid looking for neigbors
'''
def full_search(cur_x:int, cur_y:int, arr:list, N:int):
    neighbors = []
    for y, row in enumerate(arr):
        for x, col in enumerate(row):
            if manhattan_dist((cur_x, cur_y), (x,y)) <= N: 
                neighbors.append((y,x))
    return neighbors

def full_solve(arr:list, N:int):
    start_time = time.perf_counter()

    neighbors = []
    for y,row in enumerate(arr):
        for x,col in enumerate(row):
            if (col > 0): neighbors += full_search(x,y, arr, N)
    
    end_time = time.perf_counter()
    return (end_time-start_time), set(neighbors)