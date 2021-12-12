#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:49:23 2021

@author: ales
"""

net = {}

with open('input.txt', mode='r') as f:
    data = [l.strip().split('-') for l in f.readlines()]
    
    for c in data:
        if c[0] in net:
            net[c[0]].add(c[1])
        else:
            net[c[0]] = set([c[1]])
        if c[1] in net:
            net[c[1]].add(c[0])
        else:
            net[c[1]] = set([c[0]])
        

def is_upper(s):
    return s == s.upper()

def find_paths_1(paths, current_path, node):
    current_path.append(node)
    
    if node == 'end':
        paths.append(current_path)
        return
    
    for next_node in net[node]:
        if is_upper(next_node) or next_node not in current_path:
            find_paths_1(paths, list(current_path), next_node)
        

paths_1 = []

find_paths_1(paths_1, [], 'start')
print(len(paths_1))

def all_but_one(path, next_node):
    next_path = list(path)
    next_path.append(next_node)
    
    uniques = set([n for n in next_path if not(is_upper(n))])
    counters = {3: 0, 2:0, 1:0}
    for u in uniques:        
        counters[next_path.count(u)] += 1       

    return counters[2] <= 1 and counters[3] == 0

def find_paths_2(paths, current_path, node):
        
    current_path.append(node)
    
    if node == 'end':
        paths.append(current_path)
        return
    
    for next_node in net[node]:
        if (is_upper(next_node) or all_but_one(current_path, next_node)) and next_node != 'start':
            find_paths_2(paths, list(current_path), next_node)
        
paths_2 = []

find_paths_2(paths_2, [], 'start')
print(len(paths_2))