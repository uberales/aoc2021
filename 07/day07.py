#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:37:24 2021

@author: podolnik
"""

with open('input.txt', mode='r') as f:
    crabs = [int(s) for s in f.readline().strip().split(',')]
    
# part 1
    
positions = sorted(set(crabs))
max_pos = max(positions)

fuel = [(p, sum([abs(c - p) for c in crabs])) for p in range(max_pos)]

fuel.sort(key=lambda f: f[1])

print(fuel[0][1])

# part 2

fuel = [(p, sum([abs(c - p) * (abs(c - p) + 1) // 2 for c in crabs])) for p in range(max_pos)]

fuel.sort(key=lambda f: f[1])

print(fuel[0][1])