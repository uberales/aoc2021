#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:09:13 2021

@author: ales
"""

import numpy as np

with open('input.txt', mode='r') as f:
    data = np.array([[int(c) for c in list(l.strip())] for l in f.readlines()])
    

field = np.array(data)
n_r, n_c = np.shape(field)

def t2a(tup):
    return (np.array([t[0] for t in tup]), np.array([t[1] for t in tup]))

def get_neighbors(pt):
    r, c = pt
    n = []
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if r + dr >= 0 and r + dr < n_r and c + dc >= 0 and c + dc < n_c:
                n.append((r + dr, c + dc))
    
    return t2a(n)


def get_flashing(field):
    loc = np.where(field > 9)
    flashing = [(r, c) for r, c in zip(loc[0], loc[1])]
    return set(flashing)
    
n_steps = 100

tot_flashes = 0
sync_i = 0

for i in range(n_steps):
    field += 1
    
    tot_flashing = set()
    prev_flashing = set()
    
    while True:
        tot_flashing = get_flashing(field)
        new_flashing = tot_flashing.difference(prev_flashing)
        prev_flashing = tot_flashing
        
        if len(new_flashing) == 0:
            break
                
        for pt in new_flashing:
            neighbors = get_neighbors(pt)
            field[neighbors] += 1        
    
    if len(tot_flashing) > 0:
        field[t2a(list(tot_flashing))] = 0

    n_flashes = np.sum(field == 0)
    tot_flashes += n_flashes
        
    if n_flashes == n_r * n_c:
        sync_i = i

print(tot_flashes)


while True:
    field += 1
    i += 1
    
    tot_flashing = set()
    prev_flashing = set()
    
    while True:
        tot_flashing = get_flashing(field)
        new_flashing = tot_flashing.difference(prev_flashing)
        prev_flashing = tot_flashing
        
        if len(new_flashing) == 0:
            break
                
        for pt in new_flashing:
            neighbors = get_neighbors(pt)
            field[neighbors] += 1        
    
    if len(tot_flashing) > 0:
        field[t2a(list(tot_flashing))] = 0

    n_flashes = np.sum(field == 0)
        
    if n_flashes == n_r * n_c:
        break

print(i + 1)
