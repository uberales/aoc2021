#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:54:28 2021

@author: podolnik
"""

import re

with open('input.txt', mode = 'r') as f:
    t = f.readline().strip()
    m = re.match('^target area: x=([\-0-9]*)\.\.([\-0-9]*), y=([\-0-9]*)\.\.([\-0-9]*)$', t)
    x_min = int(m[1])
    x_max = int(m[2])
    y_min = int(m[3])
    y_max = int(m[4])

# part 1

def fire(v_x, v_y):
    x, y = (0, 0)
    
    h_max = 0
    
    while True:
        x += v_x
        y += v_y
        
        v_x = max(v_x - 1, 0)
        v_y = v_y - 1
        
        h_max = max(h_max, y)
    
        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            return h_max
        elif x > x_max or y < y_min:
            return None

h_vals = []

for v_x in range(500):
    for v_y in range(-500,500):
        h = fire(v_x, v_y)
        if h is not None:
            h_vals.append(((v_x, v_y), h))

h_vals.sort(key=lambda h: h[1], reverse=True)
print(h_vals[0])

# part 2
print(len(h_vals))
