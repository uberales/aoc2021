#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 11:54:12 2021

@author: ales
"""

import numpy as np

with open('test.txt', mode='r') as f:
    lines = [l.strip() for l in f.readlines()]
    scanners = []
    scanner = []
    for i, l in enumerate(lines):
        if len(l) == 0 or i == len(lines) - 1:
            scanners.append(np.array(scanner, dtype=int))
        elif l[0:3] == '---':
            scanner = []
        else:
            vals = [int(v) for v in l.split(',')]
            scanner.append(vals)
    
rot_x90 = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=int)
rot_y90 = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], dtype=int)
rot_z90 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)

test = np.array([1, 2, 3], dtype=int)

def get_rotations(vec_list, mat, n_mul = 3):
    all_r = []
    for i in range(n_mul):
        r = [np.matmul(mat, v) for v in vec_list]
        all_r.extend(r)
        mat = np.matmul(mat, mat)
    return all_r

def get_all_rotations(vec):
    # thanks https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
    r = [vec]
    r.append(np.matmul(rot_x90, vec))
    r.append(np.matmul(rot_y90, vec))
    r.append(np.matmul(rot_z90, vec))    
    r.append(np.matmul(np.matmul(rot_x90, rot_x90), vec))
    r.append(np.matmul(np.matmul(rot_x90, rot_y90), vec))
    r.append(np.matmul(np.matmul(rot_x90, rot_z90), vec))    
    r.append(np.matmul(np.matmul(rot_y90, rot_x90), vec))   
    r.append(np.matmul(np.matmul(rot_y90, rot_y90), vec))    
    r.append(np.matmul(np.matmul(rot_z90, rot_y90), vec))    
    r.append(np.matmul(np.matmul(rot_z90, rot_z90), vec))    
    r.append(np.matmul(np.matmul(np.matmul(rot_x90, rot_x90), rot_x90), vec))    
    r.append(np.matmul(np.matmul(np.matmul(rot_x90, rot_x90), rot_y90), vec))    
    r.append(np.matmul(np.matmul(np.matmul(rot_x90, rot_x90), rot_z90), vec))        
    r.append(np.matmul(np.matmul(np.matmul(rot_x90, rot_y90), rot_x90), vec))    
    r.append(np.matmul(np.matmul(np.matmul(rot_x90, rot_y90), rot_y90), vec))        
    r.append(np.matmul(np.matmul(np.matmul(rot_x90, rot_z90), rot_z90), vec))
    r.append(np.matmul(np.matmul(np.matmul(rot_y90, rot_x90), rot_x90), vec))       
    r.append(np.matmul(np.matmul(np.matmul(rot_y90, rot_y90), rot_y90), vec))    
    r.append(np.matmul(np.matmul(np.matmul(rot_z90, rot_z90), rot_z90), vec))   
    r.append(np.matmul(np.matmul(np.matmul(np.matmul(rot_x90, rot_x90), rot_x90), rot_y90), vec))     
    r.append(np.matmul(np.matmul(np.matmul(np.matmul(rot_x90, rot_x90), rot_y90), rot_x90), vec))     
    r.append(np.matmul(np.matmul(np.matmul(np.matmul(rot_x90, rot_y90), rot_x90), rot_x90), vec))     
    r.append(np.matmul(np.matmul(np.matmul(np.matmul(rot_x90, rot_y90), rot_y90), rot_y90), vec))         
    return r

def correlate(points, candidates):
    corr_table = np.zeros((len(points), len(candidates), 3), dtype = int)
    vals = []
    for p in range(len(points)):
        for c in range(len(candidates)):
            corr_table[p, c, :] = points[p] - candidates[c]
            vals.append(corr_table[p, c, :])
    unique = np.unique(vals, axis=0)
    counts = [(u, len([v for v in vals if (u == v).all()])) for u in unique]
    
    return vals, unique, sorted(counts, key=lambda c: c[1], reverse=True)

r = get_all_rotations(test)

points = np.array(scanners[0])

for i in range(1, len(scanners)):
    scanner = scanners[i]
    rotated = [get_all_rotations(vec) for vec in scanner]
    for j in range(24):
        s_ver = np.array([rotated[k][j] for k in range(len(scanner))])
        ct = correlate(points, s_ver)        
        if len(ct[0]) != len(ct[1]):
            print(j, ct[2][0])
    break

