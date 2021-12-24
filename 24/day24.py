#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 12:27:03 2021

@author: podolnik
"""

import itertools

def l2d(l):
    parts = l.split(' ')
    return tuple([int(p) if p[-1].isnumeric() else p for p in parts])

with open('input.txt', mode='r') as f:
    instructions = [l2d(l.strip()) for l in f.readlines()]

def process(instruction, registry, input_data):
    code, *operands = instruction
    if code == 'inp':
        registry[operands[0]] = input_data.pop(0)
        #print(instruction, registry[operands[0]])
    elif code == 'add':
        a = operands[0]
        b = operands[1] if type(operands[1]) is int else registry[operands[1]]
        registry[a] = registry[a] + b
    elif code == 'mul':
        a = operands[0]
        b = operands[1] if type(operands[1]) is int else registry[operands[1]]
        registry[a] = registry[a] * b
    elif code == 'div':
        a = operands[0]
        b = operands[1] if type(operands[1]) is int else registry[operands[1]]
        registry[a] = registry[a] // b
    elif code == 'mod':
        a = operands[0]
        b = operands[1] if type(operands[1]) is int else registry[operands[1]]
        registry[a] = registry[a] % b
    elif code == 'eql':
        a = operands[0]
        b = operands[1] if type(operands[1]) is int else registry[operands[1]]
        registry[a] = 1 if registry[a] == b else 0

def simplify(l):
    result = []
    
    l = l.replace('(', '( ')
    l = l.replace(')', ' )')
    l = l.replace('  ', ' ')
    parts = l.split(' ')
    level = 0
    left = False
    stack = 0
    total = 0
    for c in parts:
        if c == '(':
            level += 1
        elif c == '+':
            pass
    return(parts)

def translate(instruction, registry, input_data):

    def reg_eval(r):
        return str(registry[r]) if r in registry else str(r)
    
    def paren(a, op = None):
        a_eval = reg_eval(a)
        if op is None or op == '+':
            return a_eval
        if ' ' in a_eval:
            return '({})'.format(a_eval)
        return a_eval
    
    operators = {'add': '+', 'mod': '%', 'mul': '*', 'div': '/'}
    
    def proc_op(r, a, b, op):
        if a == '0' and b == '0':
            registry[r] = '0'
        elif a == '0':
            registry[r] = '{}'.format(paren(b))
        elif b == '0' or (b == '1' and op == '//'):
            registry[r] = '{}'.format(paren(a))
        elif b == '1' and op == '%':
            registry[r] = '0'
        else:
            registry[r] = '{} {} {}'.format(paren(a, op), op, paren(b, op))
    print(instruction)
    print(registry)
    code, *operands = instruction
    if code == 'inp':
        registry[operands[0]] = input_data.pop(0)
        print('reading', code, operands, registry[operands[0]])
    elif code in operators:
        r = operands[0]
        a = reg_eval(operands[0])
        b = reg_eval(operands[1])
        print('{}, {}, {}'.format(r, a, b))
        proc_op(r, a, b, operators[code])  
    elif code == 'eql':
        r = operands[0]
        a = reg_eval(operands[0])
        b = reg_eval(operands[1])
        print('{}, {}, {}'.format(r, a, b))
        
        if (a == '0' and b == '0') or a == b:
            registry[r] = '1'
        else:
            registry[r] = '{} == {}'.format(paren(a), paren(b), code)
    print()

def compute(input_data, instructions):
    registry = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for instruction in instructions:
        process(instruction, registry, input_data)
    return registry

def rewrite(instructions):
    registry = {'w': '0', 'x': '0', 'y': '0', 'z': '0'}
    input_data = list('abcdefghijklmn')
    for instruction in instructions:
        translate(instruction, registry, input_data)
    return registry
        
test = '13579246899999'
test_numbers = [[int(i) for i in '13579246899999']]
numbers = itertools.product([i for i in range(1, 10)], repeat=14)
valid = []
max_n = 0

i = 0
for n in numbers:
    input_data = list(n)
    reg = compute(input_data, instructions)
    if reg['z'] == 0:
        valid.append(int(''.join([str(i) for i in n])))
        max_n = max(max_n, int(''.join([str(d) for d in n])))
    i += 1

    if i % 100000 == 0:
        print(i)