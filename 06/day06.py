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

def next_day(states):   
    s_0 = states.pop(0)
    states[6] += s_0
    states.append(s_0)
    
n_days = 256
states = [0 for i in range(9)]
for f in data:
    states[f] += 1
    
for i in range(n_days):
    next_day(states)
    
print('Day {}: {} fish in the school'.format(n_days, sum(states)))