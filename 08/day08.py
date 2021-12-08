#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:01:02 2021

"""

def l2d(line):
    parts = line.strip().split(' | ')
    pattern = parts[0].strip().split(' ')
    value = parts[1].strip().split(' ')
    return (pattern, value)

with open('input.txt', mode='r') as f:
    data = [l2d(l) for l in f.readlines()]

segments = 'abcdefg'
base_pattern = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

# part 1

def get_len_match(pattern): 
    len_match = {}
    for i, n in enumerate(pattern):
        if len(n) in len_match:
            len_match[len(n)].append(i)
        else:
            len_match[len(n)] = [i]
    return len_match

len_match = get_len_match(base_pattern)
counter = sum([sum([1 for v in d[1] if len(len_match[len(v)]) == 1]) for d in data])
            
print(counter)

# part 2

def get_seg_match(pattern):
    seg_count = {s: list(''.join(pattern)).count(s) for s in segments}
    seg_len_match = {}
    
    for s, n in seg_count.items():
        if n in seg_len_match:
            seg_len_match[n].append(s)
        else:
            seg_len_match[n] = [s]
    return seg_len_match

seg_match = get_seg_match(base_pattern)

def filter_matching(p_local, p_base, permutation):    
    for l in permutation:
        b = permutation[l]
        if b is not None:
            p_local = p_local.replace(l, '')
            p_base = p_base.replace(b, '')
        
    return p_local, p_base    
       
def untangle(display):
    global seg_match, base_pattern
    
    local_pattern = display[0]
    values = display[1]
    
    permutation = {s: None for s in segments}
    
    local_seg_match = get_seg_match(local_pattern)
    local_len_match = get_len_match(local_pattern)
    
    for n, v in local_seg_match.items():
        if len(v) == 1:
            permutation[v[0]] = seg_match[n][0]
        
    for d in (1, 4, 7, 9):
        p_local = local_pattern[local_len_match[len(base_pattern[d])][0]]
        l, b = filter_matching(p_local, base_pattern[d], permutation)
        permutation[l] = b
    
    untangled = []
    for v in values:
        d = ''.join(sorted([permutation[s] for s in v]))
        untangled.append(base_pattern.index(d))
        
    return int(''.join([str(u) for u in untangled]))

total = sum([untangle(d) for d in data])
print(total)