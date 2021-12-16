#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:51:15 2021

"""

import numpy as np

def h2b(c):
    i = int(c, 16)    
    return "{:04b}".format(i)

with open('input.txt', mode='r') as f:
    data = ''.join([h2b(c) for c in f.readline().strip()])
    
# part 1

total = 0

def read_packets(bin_str, packets, limit = None):
    global total
    if '1' not in bin_str:
        return ''
    
    version = int(bin_str[0:3], 2)
    
    total += version
    
    type_id = int(bin_str[3:6], 2)
    value = None
    payload = []
    
    remainder = ''
    
    if type_id == 4:
        pos = 6
        read = ''
        while True:
            bits = bin_str[pos:pos+5]
            read += bits[1:]
            pos += 5
            if bits[0] == '0':
                break
        value = int(read, 2)
        
        remainder = bin_str[pos:]
    else:
        length_id = int(bin_str[6], 2)
        if length_id == 0:
            length = int(bin_str[7:7+15], 2)
        
            payload_str = bin_str[7+15:7+15+length]
            
            read_packets(payload_str, payload)            
            remainder = bin_str[7+15+length:]
            
        elif length_id == 1:
            count = int(bin_str[7:7+11], 2)
            payload_str = bin_str[7+11:]
                        
            remainder = read_packets(payload_str, payload, count)
               
    packet = {'version': version, 'type_id': type_id, 'value': value, 'payload': payload}
    packets.append(packet)
    
    if len(remainder) > 0:
        if (limit is not None and limit > 1):
            return read_packets(remainder, packets, limit - 1)
        elif limit is None:
            return read_packets(remainder, packets)
    
    return remainder

packets = []
read_packets(data, packets)
print(total)

# part 2

def evaluate(packet):
    tid = packet["type_id"]
    if tid == 0:
        value = sum([evaluate(p) for p in packet["payload"]])
    elif tid == 1:
        value = np.prod([evaluate(p) for p in packet["payload"]])
    elif tid == 2:
        value = min([evaluate(p) for p in packet["payload"]])
    elif tid == 3:
        value = max([evaluate(p) for p in packet["payload"]])
    elif tid == 4:
        value = packet["value"]
    elif tid == 5:
        v_0 = evaluate(packet["payload"][0])
        v_1 = evaluate(packet["payload"][1])
        value = 1 if v_0 > v_1 else 0
    elif tid == 6:
        v_0 = evaluate(packet["payload"][0])
        v_1 = evaluate(packet["payload"][1])
        value = 1 if v_0 < v_1 else 0
    elif tid == 7:
        v_0 = evaluate(packet["payload"][0])
        v_1 = evaluate(packet["payload"][1])
        value = 1 if v_0 == v_1 else 0
        
    return value
    
val = evaluate(packets[0])
print(val)