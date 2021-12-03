#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:26:11 2021

"""

import numpy as np

with open('input.txt', mode='r') as f:
    data = np.array([[int(s) for s in list(l.strip())] for l in f.readlines()])


def get_bits(numbers):
    n_lines = len(numbers)
    most = [sum(numbers[:,i]) >= n_lines / 2 for i in range(len(numbers[0]))]
    least = [~b for b in most]
    return (least, most)

def b2d(bits):
    return sum([2**i * int(bits[-i-1]) for i in range(len(bits))])

bits = get_bits(data)

gamma = b2d(bits[1])
epsilon = b2d(bits[0])

print(gamma * epsilon)

def filter_numbers(numbers, most_least, position = 0):
    if len(numbers) == 1:
        return numbers[0]
    
    bits = get_bits(numbers)
    idx = numbers[:,position] == bits[most_least][position]
    
    return filter_numbers(numbers[idx,:], most_least, position = position + 1)

oxygen_b = filter_numbers(data, 1)
oxygen = b2d(oxygen_b)

dioxide_b = filter_numbers(data, 0)
dioxide = b2d(dioxide_b)

print(oxygen*dioxide)