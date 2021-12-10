#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:34:13 2021

"""

with open('input.txt', mode='r') as f:
    data = [l.strip() for l in f.readlines()]

opening = '([{<'
closing = ')]}>'
scores_1 = {')': 3, ']': 57, '}': 1197, '>': 25137}

def purge(line):
    len_0 = len(line)
    while True:
        for i in range(4):
            line = line.replace('{}{}'.format(opening[i], closing[i]), '')
        
        if len(line) == len_0:
            return line
        
        len_0 = len(line)
    
def get_illegal(line):
    indices = [(line.index(c), c) for c in closing if c in line]
    return sorted(indices, key=lambda i: i[0])
               

illegals = [get_illegal(purge(line)) for line in data]
points = [scores_1[il[0][1]] for il in illegals if len(il) > 0]
print(sum(points))
    

def get_closing(line):
    return ''.join([closing[opening.index(line[-i - 1])] for i in range(len(line))])

scores_2 = {')': 1, ']': 2, '}': 3, '>': 4}
def get_score(closing_line):
    total = 0
    for c in closing_line:
        total = total * 5
        total += scores_2[c]
    return total
    

incomplete = [purge(data[i]) for i in range(len(illegals)) if len(illegals[i]) == 0]
points = sorted([get_score(get_closing(line)) for line in incomplete])
print(points[len(points)//2])
