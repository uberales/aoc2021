#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:10:04 2021

@author: ales
"""

import copy

with open('test.txt', mode='r') as f:
    data = [list(l.strip()) for l in f.readlines()]
    
hall_r = 1
hall_c = list(range(1,len(data[0])-1))

home_r = [3, 2]
home_c = [3, 5, 7, 9]

kind = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def get_distance(r_1, c_1, r_2, c_2):
    return abs(r_1 - r_2) + abs(c_1 - c_2)

def show(field, overlay = set()):
    for r in range(len(field)):
        s = ''
        for c in range(len(field[r])):
            if (r, c) in overlay:
                s += '*'
            else:
                s += field[r][c]
        print(s)

def check_avail(field, r_1, c_1, r_2, c_2):
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    reached = set([(r_1, c_1)])
    n_reached = 0
    while True:
        new_reached = set()
        for dest in reached:
            for d in dirs:
                r = dest[0] + d[0]
                c = dest[1] + d[1]
                if field[r][c] == '.':
                    new_reached.add((r, c))
        reached = reached.union(new_reached)
        if len(reached) == n_reached:
            break
        n_reached = len(reached)    
    
    reached.remove((r_1, c_1))    
    
    return (r_2, c_2) in reached
                

def get_avail(field, p, r, c):
    avail = []
    loc = None
    if r == hall_r:
        c_1 = home_c[players[p]]
        for r_1 in home_r:
            if field[r_1][c_1] == '.':
                if check_avail(field, r, c, r_1, c_1):
                    avail.append((r_1, c_1))
                    loc = 'home'
                break
            elif field[r_1][c_1] != p:
                break
    elif c in home_c:
        r_1 = hall_r
        for c_1 in hall_c:
            if c_1 not in home_c and check_avail(field, r, c, r_1, c_1):
                avail.append((r_1, c_1))
                loc = 'hall'
                            
    return loc, avail

def get_players(field):
    players = []
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] in kind.keys():
                players.append((field[r][c], r, c))
                
    if len(players) != 8:
        raise NotImplementedError()
    return players

def all_home(field):
    for k in kind:
        c = home_c[kind[k]]
        for r in home_r:
            if field[r][c] != k:
                return False
    return True

field = copy.deepcopy(data)
players = get_players(field)

for p in players:
    loc, avail = get_avail(field, p[0], p[1], p[2])
    print(loc, avail)

print(all_home(field))
        