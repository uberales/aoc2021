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


def find_paths_2(paths, current_path, node, double_found = False):
    current_path.append(node)
    
    if node == 'end':
        paths.append(current_path)
        return
    
    for next_node in net[node]:
        if is_upper(next_node):
            find_paths_2(paths, list(current_path), next_node, double_found)
        elif next_node != 'start':            
            if double_found:
                if next_node not in current_path:
                    find_paths_2(paths, list(current_path), next_node, double_found)
            else:
                if current_path.count(next_node) <= 1:
                    find_paths_2(paths, list(current_path), next_node, current_path.count(next_node) == 1)
                
                
                        
paths_2 = []

find_paths_2(paths_2, [], 'start')
print(len(paths_2))