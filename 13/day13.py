#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:36:15 2021

"""

import re

with open('input.txt', mode='r') as f:
    text = f.read()
    data = re.findall('([0-9]*),([0-9]*)', text)
    data = [(int(r[0]), int(r[1])) for r in data]
    
    folds = re.findall('fold along ([xy])=([0-9]*)', text)
    folds = [(r[0], int(r[1])) for r in folds]
    
# part 1

def show(grid):
    m0 = max([p[0] for p in grid])
    m1 = max([p[1] for p in grid])
    for y in range(m1 + 1):
        s = ''
        for x in range(m0 + 1):
            if (x, y) in grid:
                s += '#'
            else:
                s += ' '
        print(s)

def fold(pt, axis, loc):
    x = pt[0]
    y = pt[1]
    if axis == 'x' and x > loc:
        x = 2 * loc - x
    if axis == 'y' and y > loc:
        y = 2 * loc - y
    return (x, y)
    
grid = set(data)
grid = set([fold(pt, folds[0][0], folds[0][1]) for pt in grid])

print(len(grid))

# part 2

for i in range(1, len(folds)):
    grid = set([fold(pt, folds[i][0], folds[i][1]) for pt in grid])

show(grid)    
