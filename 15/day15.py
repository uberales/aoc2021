#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:48:22 2021

"""

import numpy as np

with open('input.txt', mode='r') as f:
    data = np.array([[int(c) for c in list(l.strip())] for l in f.readlines()])
    
# part 1    

n_r = len(data)
n_c = len(data[0])

def get_neighbors_next(pt):
    return get_neighbors(pt, dirs = [(1, 0), (0, 1)])    

def get_neighbors_prev(pt):
    return get_neighbors(pt, dirs = [(-1, 0), (0, -1)])

def get_neighbors(pt, dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]):
    r, c = pt
    n = []
    
    for dr, dc in dirs:
        if r + dr >= 0 and r + dr < n_r and c + dc >= 0 and c + dc < n_c:
            n.append((r + dr, c + dc))
    
    return n

def seed(data):
    n_r = len(data)
    n_c = len(data[0])
    
    minima = np.zeros(np.shape(data), dtype=int)   
    
    for d in range(1, 2 * n_c - 1):
        pt = (d, 0)
        for i in range(d + 1):
            if pt[0] < n_r and pt[1] < n_c:
                minima[pt[0], pt[1]] = min([minima[n[0],n[1]] + data[pt[0],pt[1]] for n in get_neighbors_prev(pt)])
            pt = (pt[0] - 1, pt[1] + 1)
    return minima

def settle(minima):
    while True:
        flips = 0
        for r in range(0, n_r):
            for c in range(0, n_c):
                pt = (r, c)
                for n in get_neighbors(pt):
                    if minima[r, c] > minima[n[0], n[1]] + data[r, c]:
                        minima[r, c] = minima[n[0], n[1]] + data[r, c]
                        flips += 1
        if flips == 0:
            break
        
minima = seed(data)
settle(minima)

print(minima[-1,-1])

# part 2

def get_part_2(data):
    data_2 = np.zeros((n_r*5, n_c*5), dtype=int)
    data_2[0:n_r,0:n_c] = data
    
    temp = np.array(data)
    
    for r in range(1, 5):
        temp = temp + 1
        temp[temp == 10] = 1
        data_2[n_r * r:n_r * (r + 1),0:n_c] = temp
    
    temp = data_2[:,0:n_c]
    
    for c in range(1, 5):
        temp = temp + 1
        temp[temp == 10] = 1
        data_2[:,n_c * c:n_c * (c + 1)] = temp

    return data_2

data = get_part_2(data)
n_r = len(data)
n_c = len(data[0])

minima = seed(data)
settle(minima)

print(minima[-1,-1])