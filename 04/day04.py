#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:50:50 2021

"""

import numpy as np
import copy

with open('input.txt', mode='r') as f:
    numbers = [int(s) + 1 for s in f.readline().strip().split(',')] # increase numbers by one to make checking easier
    f.readline()
    tables = []
    current = []
    l = f.readline()    
    while True:
        tl = [int(s) + 1 for s in l.strip().split(' ') if s] # plus one trick
        l = f.readline()
        
        if len(tl) == 0:
            tables.append(np.array(current))
            current = []
        else:
            current.append(tl)
        
        if not l:
            break
    
    if len(current) > 0:
        tables.append(np.array(current))
        
def score(board):
    unmarked = board[board > 0]
    return sum(unmarked) - len(unmarked)
    
def check(board):
    for i in range(5):
        if sum(board[:,i]) == 0 or sum(board[i,:]) == 0:
            return True
    return False

# part 1

tables_1 = copy.deepcopy(tables)

for n in numbers:
    try:
        for t in tables_1:
            t[t == n] = 0
            if check(t):
                print(score(t) * (n - 1))
                raise(StopIteration())
    except StopIteration:
        break

# part 2

tables_2 = copy.deepcopy(tables)

for n in numbers:
    pop = []
    for i, t in enumerate(tables_2):
        t[t == n] = 0
        if check(t):
            print(score(t) * (n - 1))
            pop.append(i)
            
    pop.sort(reverse=True)
    for i in pop:
        tables_2.pop(i)