#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:10:09 2021

"""

directions = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}

def l2d(l):
    p = l.strip().split(' ')
    return (directions[p[0]], int(p[1]))

with open('input.txt', mode='r') as f:
    data = [l2d(l) for l in f.readlines()]

# part 1

dx, dy = zip(*[(d[0][0]*d[1], d[0][1]*d[1]) for d in data])

x = sum(dx)
y = sum(dy)

print(x*y)

# part 2

# keep the x from previous part
y = 0
a = 0

for i in range(len(dx)):
    dxi = dx[i]
    dxy = dy[i]
    if dxi > 0:
        y += dxi * a
    else:
        a = a + dxy
        
print(x*y)