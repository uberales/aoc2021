#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:13:40 2021

@author: ales
"""

import re

def l2n(line):
    line = line.replace('[', '[,')
    line = line.replace(']', ',]')
    line = line.replace(',,', ',')
    return [int(c) if c.isnumeric() else c for c in line.split(',')]

with open('input.txt', mode='r') as f:
    data = [l2n(l.strip()) for l in f.readlines()]

# part 1

def n2l(number):
    line = ','.join([str(n) for n in number])
    line = line.replace('[,', '[')
    line = line.replace(',]', ']')
    return line        

def add(left, right):
    result = ['[']
    result.extend(left)
    result.extend(right)
    result.append(']')
    return result
    
def get_exploding(number):
    level = 0
    for i in range(len(number)):
        c = number[i]
        if c == '[':
            level += 1
        elif c == ']':
            level -= 1
        if level == 5:
            return i
    return -1

def get_splitting(number):
    for i in range(len(number)):
        if type(number[i]) is int and number[i] > 9:
            return i
    return -1
        
def explode(n, i):    
    if i >= 0:
        n_l = n[i + 1]
        n_r = n[i + 2]
        for j in range(i, 0, -1):
            if type(n[j]) is int:
                n[j] += n_l
                break
        for j in range(i + 3, len(n)):
            if type(n[j]) is int:
                n[j] += n_r
                break
        for j in range(i + 2, i - 1, -1):
            n.pop(j)
        n[i] = 0
        return n
    return n

def split(n, i):
    if i >= 0:
        lower = n[i] // 2
        upper = n[i] - lower
        result = ['[', lower, upper, ']']
        n.pop(i)
        for j in range(len(result)):
            n.insert(i + j, result[j])        
    return n

def reduce(n):
    while True:
        e_i = get_exploding(n)
        if e_i > 0:
            explode(n, e_i)
            continue
        
        s_i = get_splitting(n)
        if s_i > 0:
            split(n, s_i)
            continue
    
        break
    return n

def magnitude(n):
    s = n2l(n)
    while True:
        m = re.findall('\[([0-9]*)\,([0-9]*)\]',s)
        if len(m) == 0:
            break
        for g in m:
            v = 3 * int(g[0]) + 2 * int(g[1])
            s = s.replace('[{},{}]'.format(g[0], g[1]), '{}'.format(v))            
    
    return int(s)
    
    
n = data[0]
for i in range(1, len(data)):
    n = add(n, data[i])
    n = reduce(n)

print(n2l(n))

m = magnitude(n)

print(m)

# part 2

m_max = 0

for i in range(len(data)):
    for j in range(len(data)):       
        if j != i:
            m = magnitude(reduce(add(data[i], data[j])))
            if m > m_max:
                m_max = m

print(m_max)