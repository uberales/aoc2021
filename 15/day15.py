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

def get_neighbors(pt, dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)], r_max = n_r, c_max = n_c):
    r, c = pt
    n = []
    
    for dr, dc in dirs:
        if r + dr >= 0 and r + dr < r_max and c + dc >= 0 and c + dc < c_max:
            n.append((r + dr, c + dc))
    
    return n

def search(data):
    n_r = len(data)
    n_c = len(data[0])
    
    minima = np.zeros(np.shape(data), dtype=int)
    
    to_search = set([(0, 0)])
    
    while len(to_search) > 0:
        next_search = set([])
        
        for pt in to_search:
            for n in get_neighbors(pt, r_max = n_r, c_max = n_c):                
                if minima[n[0], n[1]] == 0:
                    minima[n[0], n[1]] = minima[pt[0], pt[1]] + data[n[0], n[1]] 
                    next_search.add(n)
                else:                    
                    d_prev = minima[n[0], n[1]]
                    d_next = minima[pt[0], pt[1]] + data[n[0], n[1]]
                    if d_prev > d_next:
                        minima[n[0], n[1]] = d_next
                        next_search.add(n)
        to_search = next_search
    
    return minima
    
        
minima = search(data)

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

minima = search(data)

print(minima[-1,-1])