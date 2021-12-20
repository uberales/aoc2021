#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:35:36 2021

"""

import numpy as np

with open('input.txt', mode='r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    rules = np.array([c == '#' for c in lines[0]])
    
    image = np.array([[c == '#' for c in l] for l in lines[2:]])
    
# part 1
    
def sq2i(square):
    return int(''.join(['1' if c else '0' for c in np.array(square).flatten()]), 2)

def show(image):
    for row in image:
        s = ''
        for c in row:
            s += '#' if c else '.'
        print(s)

def iterate(image, rules, parity):
    sh = np.shape(image)
    mask_image = np.zeros((sh[0]+4, sh[1]+4), dtype=bool)
    mask_image[:] = parity
    mask_image[2:-2,2:-2] = image
    next_image = np.array(mask_image)
    
    for r in range(1, len(mask_image) - 1):
        for c in range(1, len(mask_image[0]) - 1):            
            sq = mask_image[r-1:r+2,c-1:c+2]
            idx = sq2i(sq)
            next_image[r, c] = rules[idx]
            
    return next_image[1:-1,1:-1]
            
n_iter = 2
image_1 = np.array(image)

for i in range(n_iter):
    image_1 = iterate(image_1, rules, i % 2 or not(rules[0]))
    
print(np.sum(image_1))

# part 2
                        
n_iter = 50
image_2 = np.array(image)

for i in range(n_iter):
    image_2 = iterate(image_2, rules, i % 2 or not(rules[0]))
    
print(np.sum(image_2))
            
    