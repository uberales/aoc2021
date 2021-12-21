#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:00:15 2021

"""

from pprint import pprint

with open('input.txt', mode='r') as f:
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


def sums_tot(n):
    all_sums = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                all_sums.append(i+j+k)
    return all_sums

def sums(n):
    all_sums = sums_tot(n)
    uniques = list(set(all_sums))
    return uniques, [len([s for s in all_sums if s == u]) for u in uniques]

all_sums, multiplicities = sums(3)

cache = {}

def play_2(state):
    if state in cache:
        return cache[state]
    wins = [0, 0]        
    states = [state]
    
    while len(states) > 0:
        state = states.pop(0)
        # pprint(state)
        
        for r, m in zip(all_sums, multiplicities):
            pid = state[0]
            
            pos = (state[pid * 2 + 1] + r) % 10
            sco = state[pid * 2 + 2] + pos + 1
            mul = state[5] * m
            
            if sco >= 21:
                wins[pid] += mul
            else:
                next_state = ()
                if pid == 0:
                    next_state = (1, pos, sco, state[3], state[4], mul)
                else:
                    next_state = (0, state[1], state[2], pos, sco, mul)
                    
                r_wins = play_2(next_state)
                wins[0] += r_wins[0]
                wins[1] += r_wins[1]
    
    if state not in cache:
        cache[state] = wins
        
    return wins

wins = play_2((0, pos_a, 0, pos_b, 0, 1))
print(max(wins))