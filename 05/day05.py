#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:37:56 2021

"""

import re

with open('input.txt', mode='r') as f:
    matches = re.findall('([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)', f.read())
    data = [((int(m[0]), int(m[1])), (int(m[2]), int(m[3]))) for m in matches]
    
def get_points(c0, c1, diagonal = False):    
    diff_x = 1 if c1[0] > c0[0] else -1
    diff_y = 1 if c1[1] > c0[1] else -1

    if c0[0] == c1[0]:
        return [(c0[0], y) for y in range(c0[1], c1[1] + diff_y, diff_y)]
    if c0[1] == c1[1]:
        return [(x, c0[1]) for x in range(c0[0], c1[0] + diff_x, diff_x)]
    
    if diagonal:
        diff_x = 1 if c1[0] > c0[0] else -1
        diff_y = 1 if c1[1] > c0[1] else -1
        return [(x, y) for x, y in zip(range(c0[0], c1[0] + diff_x, diff_x), range(c0[1], c1[1] + diff_y, diff_y))]
        
    
    return []
    
field = {}

for i, source in enumerate(data):
    points = get_points(source[0], source[1])
    
    for pt in points:
        if pt in field:
            field[pt].append(i)
        else:
            field[pt] = [i]

overlapping = [pt for pt in field if len(field[pt]) > 1]

print(len(overlapping))
    

field = {}

for i, source in enumerate(data):
    points = get_points(source[0], source[1], diagonal = True)
    
    for pt in points:
        if pt in field:
            field[pt].append(i)
        else:
            field[pt] = [i]

overlapping = [pt for pt in field if len(field[pt]) > 1]

print(len(overlapping))
    