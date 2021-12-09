#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:58:02 2021

"""

import numpy as np

with open('input.txt', mode='r') as f:
    data = np.array([[int(s) for s in list(l.strip())] for l in f.readlines()])

# part 1

sh = np.shape(data)

ext_arr = np.zeros((sh[0]+ 2, sh[1] + 2))

ext_arr[1:-1,1:-1] = data

ext_arr[0,1:-1] = data[1,:]
ext_arr[-1,1:-1] = data[-2,:]
ext_arr[1:-1,0] = data[:,1]
ext_arr[1:-1,-1] = data[:,-2]

dc_r = ext_arr[1:-1, :-2] - ext_arr[1:-1,1:-1]
dc_l = ext_arr[1:-1, 1:-1] - ext_arr[1:-1,2:]

dr_l = ext_arr[:-2, 1:-1] - ext_arr[1:-1, 1:-1]
dr_u = ext_arr[1:-1, 1:-1] - ext_arr[2:, 1:-1]

minima = (dc_l < 0) & (dc_r > 0) & (dr_u < 0) & (dr_l > 0)

risk_levels = sum(data[minima]) + np.sum(minima)
print(risk_levels)

# part 2

r_max, c_max = np.shape(data)

def neighbors(r, c):
    n = []
    if r > 0:
        n.append((r-1, c))
    if c > 0:
        n.append((r, c - 1))
    if r < r_max - 1:
        n.append((r + 1, c))
    if c < c_max - 1:
        n.append((r, c + 1))
    return n

def inspect_basin(point, all_points):
    if point in all_points or data[point] == 9:
        return
        
    all_points.add(point)
    for n in neighbors(point[0], point[1]):
        inspect_basin(n, all_points)
    

positions = np.where(minima)
basins = []

for r, c in zip(positions[0], positions[1]):
    basin = set([])
    inspect_basin((r, c), basin)
    basins.append(basin)

basins.sort(key=lambda b: len(b), reverse=True)

print(len(basins[0]) * len(basins[1]) * len(basins[2]))