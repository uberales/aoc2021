#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:37:27 2021

"""

import os
import matplotlib.pyplot as plt
import numpy as np

days = []
lines = []

days_f90 = []
lines_f90 = []

def loc_py(file_path):
    pt1_loc = 0
    pt2_loc = 0
    with open(file_path, mode='r') as f:
        loc = 0
        counting = True
        for l in f.readlines():
            l = l.strip()            
            if l[0:3] == '"""' and counting:
                counting = False
            elif l[0:3] == '"""':
                counting = True
                continue
            
            if counting:
                if len(l) > 0 and l[0] != "#":
                    loc += 1
                    
            if l.replace(' ', '') == '#part1':
                pt1_loc = loc
                
            if l.replace(' ', '') == '#part2':
                pt2_loc = loc
            
    return [loc, pt1_loc, pt2_loc - pt1_loc, loc - pt2_loc]

def loc_f90(file_path):
    loc = 0
    with open(f90_path, mode='r') as f:
        loc = sum([1 for l in f.readlines() if len(l.strip()) > 0 and l.strip()[0] != "!"])
    return loc

for i in range(25):
    py_path = '{0:02d}/day{0:02d}.py'.format(i+1)
    if os.path.exists(py_path):
        days.append(i+1)        
        lines.append(loc_py(py_path))
        print(py_path)
        
    f90_path = '{0:02d}/day{0:02d}.f90'.format(i+1)
    if os.path.exists(f90_path):
        days_f90.append(i+1)
        lines_f90.append(loc_f90(py_path))
        print(f90_path)

days = np.array(days)
lines = np.array(lines)
days_f90 = np.array(days_f90)
lines_f90 = np.array(lines_f90)

w = 0.45
tics = list(range(1,int(max(max(days), max(days_f90))+1)))

plt.figure()

plt.bar(days - w/2, lines[:,2], width = w, label='Python, #1')
plt.bar(days - w/2, lines[:,3], bottom = lines[:,2], width = w, label='Python, #2', color='tab:blue', alpha=0.5)
plt.bar(days - w/2, lines[:,1], bottom = lines[:,2] + lines[:,3], width = w, label='Python IO', color='tab:grey', alpha=0.25)

plt.bar(days_f90 + w/2, lines_f90, width = w, label='Fortran')
plt.xlabel('Day')
plt.xticks(tics)
plt.ylabel('SLOC')
plt.title('Lines of code in AOC 2021')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig('loc.png', bbox_inches='tight')
plt.show()