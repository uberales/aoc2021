#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:18:46 2021

"""

import copy

with open('input.txt', mode='r') as f:
    data = [int(s) for s in f.readline().strip().split(',')]
    

def get_school(data, n_days):
    school = copy.deepcopy(data)
    new_count = 0
    
    for i in range(n_days):
        # after one day
        school = [(f - 1) % 7 if f < 7 else f - 1 for f in school]
        new_fish = [8 for _ in range(new_count)]
        school.extend(new_fish)        
        
        new_count = sum([1 for s in school if s == 0])

    return school

n_days = 80
school = get_school(data, n_days)

print('Day {}: {} fish in the school'.format(n_days, len(school)))

def ceil_div(a, b):
    return -(a // (-b))

def count_produced(n_days, init_state):    
    new_count = ceil_div(n_days - init_state, 7)
    if new_count <= 0:
        return 0
    
    init_states = [7 * i + init_state + 1 + 8 for i in range(new_count)]
    generations = [count_produced(n_days, state) for state in init_states]
    return new_count + sum(generations)

n_days = 256
school = copy.deepcopy(data)
uniques = list(set(school))

cache = {u: 1 + count_produced(n_days, u) for u in uniques}

total = sum([cache[f] for f in school])

print('Day {}: {} fish in the school'.format(n_days, total))
