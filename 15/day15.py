#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:48:22 2021

"""

import numpy as np

with open('test.txt', mode='r') as f:
    data = np.array([[int(c) for c in list(l.strip())] for l in f.readlines()])
    
n_r = len(data)
n_c = len(data[0])

def t2a(tup):
    return (np.array([t[0] for t in tup]), np.array([t[1] for t in tup]))

def get_neighbors(pt):
    r, c = pt
    n = []
    
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if r + dr >= 0 and r + dr < n_r and c + dc >= 0 and c + dc < n_c:
            n.append((r + dr, c + dc))
    
    return n

top_left = (0, 0)
bottom_right = (n_r - 1, n_c - 1)

def show(grid):
    m0 = max([p[0] for p in grid])
    m1 = max([p[1] for p in grid])
    for y in range(m1 + 1):
        s = ''
        for x in range(m0 + 1):
            if (y, x) in grid:
                s += '{}'.format(data[y, x])
            else:
                s += ' '
        print(s)

def get_string(init_pt, target_pt, path):
    stairs = [(1, 0), (0, 1)]
    last = init_pt
    i = 0
    while last[0] != target_pt[0] or last[1] != target_pt[1]:
        last = (last[0] + stairs[i % 2][0], last[1] + stairs[i % 2][1])
        path.append(last)        
        i += 1
    return path

def get_risk(path):
    return np.sum(data[t2a(path)])  - data[0,0]

def update(path, risk):
    for i in range(len(path) - 2):
        n_0 = set(get_neighbors(path[i]))
        n_2 = set(get_neighbors(path[i + 2]))
        common = n_0.intersection(n_2)
        updates = [(path, risk)]
        for n_1 in common:
            new_path = list(path)
            new_path[i + 1] = n_1
            updates.append((new_path, get_risk(new_path)))

        updates.sort(key=lambda r: r[1])
                
        if updates[0][1] < risk:
            return updates[0]
    return (path, risk)

path = get_string(top_left, bottom_right, [top_left])
risk = get_risk(path)


while True:
    result = update(path, risk)
    if risk == result[1]:
        break
    
    path = result[0]
    risk = result[1]
    
show(path)
print(risk)