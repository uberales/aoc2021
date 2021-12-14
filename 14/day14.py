#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:58:52 2021

"""

import re
import copy

with open('input.txt', mode='r') as f:
    text = f.read()
    init_state = list(re.findall('^([A-Z]*)\n', text)[0])
    rules = {r[0]: r[1] for r in re.findall('([A-Z]{2}) -> ([A-Z])', text)}

# part 1

def expand_1(state, rules):
    extensions = list()
    for i in range(len(state) - 1):
        pair = ''.join(state[i:i+2])
        if pair in rules:
            extensions.append((i + 1, rules[pair]))
    
    n_ext = len(extensions)
    for i in range(n_ext):
        ext = extensions[n_ext - i - 1]
        state.insert(ext[0], ext[1])
    
def get_positions(char, string):
    return [p for p, c in enumerate(string) if c == char]
    
def count_1(state):
    uniques = set(state)
    counts = [(u, len(get_positions(u, state))) for u in uniques]
    return sorted(counts, key = lambda c: c[1])

state_1 = copy.deepcopy(init_state)
n_steps = 10
for i in range(n_steps):
    expand_1(state_1, rules)
    
counts = count_1(state_1)
print(counts[-1][1] - counts[0][1])

# part 2

def get_occurences(text, s):
    return len(re.findall('(?={0})'.format(re.escape(s)), text))

def expand_2(doubles, rules):
    def add_double(add_to, add_what, add_n):
        if add_what in add_to:
            add_to[add_what] += add_n
        else:
            add_to[add_what] = add_n
        
    new_doubles = {}
    
    for d in doubles:
        if d[0] in rules:
            d1 = (d[0][0] + rules[d[0]], d[1], False)
            d2 = (rules[d[0]] + d[0][1], False, d[2])
            
            add_double(new_doubles, d1, doubles[d])
            add_double(new_doubles, d2, doubles[d])
                
            doubles[d] = 0
        
    for d in new_doubles:
        add_double(doubles, d, new_doubles[d])

def count_2(doubles):
    letters = {l: 0 for l in set(list(''.join([k[0] for k in doubles.keys()])))}
    for d in doubles:
        letters[d[0][0]] += doubles[d]
        letters[d[0][1]] += doubles[d]
        if d[1]:
            letters[d[0][0]] += 1
        if d[2]:
            letters[d[0][1]] += 1
        
    for l in letters:
        letters[l] = letters[l] // 2
        
    counts = [(l, letters[l]) for l in letters]
    
    return sorted(counts, key = lambda c: c[1])

state_2 = ''.join(copy.deepcopy(init_state))
doubles = {(state_2[i:i+2], i == 0, i + 2 == len(state_2)): get_occurences(state_2, state_2[i:i+2]) for i in range(len(state_2) - 1)}

n_steps = 40
for i in range(n_steps):
    expand_2(doubles, rules)

counts = count_2(doubles)
print(counts[-1][1] - counts[0][1])