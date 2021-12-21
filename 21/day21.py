#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:00:15 2021

"""

from pprint import pprint

with open('test.txt', mode='r') as f:
    positions = [int(l.strip().split(' ')[-1]) for l in f.readlines()]
    
def roll(n):
    return sum([i for i in range(n + 1, n + 4)]), (n + 3) % 100

def play_1(pos_a, pos_b):    
    score_a = 0
    score_b = 0
        
    i = 0
    n = 0
    
    while True:
        
        r, n = roll(n)    
        pos_a = (pos_a + r) % 10
        score_a += pos_a + 1
        i += 3
        
        if score_a >= 1000:
            break
        
        r, n = roll(n)    
        pos_b = (pos_b + r) % 10
        score_b += pos_b + 1
        i += 3
            
        if score_a >= 1000:
            break
                
    return i*min(score_a, score_b)

pos_a = positions[0] - 1
pos_b = positions[1] - 1
print(play_1(pos_a, pos_b))

def play_2(pos_a, pos_b):
    wins = {'a': 0, 'b': 0}
    
    other = {'a': 'b', 'b': 'a'}
    
    states = [{'turn': 'a', 'a': (pos_a, 0), 'b': (pos_b, 0), 'mul': 1}]
    
    while len(states) > 0:
        state = states.pop(0)
        pprint(state)
        
        for r in range(1, 4):
            pid = state['turn']
            oid = other[pid]
            
            pos = (state[pid][0] + r) % 10
            sco = state[pid][1] + pos + 1
            
            if sco >= 21:
                wins[pid] += 1
                print(f'{pid} wins')
            else:
                new_state = {'turn': oid, pid: (pos, sco), oid: state[oid], 'mul': state['mul'] + 1}
                states.append(new_state)
        
    return wins

pos_a = positions[0] - 1
pos_b = positions[1] - 1
wins = play_2(pos_a, pos_b)
print(max(wins.values()))
            
        
        