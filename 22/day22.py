#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:44:41 2021

"""

import re

with open('input.txt', mode='r') as f:
    text = f.read()
    data = re.findall('([onf]*) x=([\-0-9]*)\.\.([\-0-9]*),y=([\-0-9]*)\.\.([\-0-9]*),z=([\-0-9]*)\.\.([\-0-9]*)', text)
    data = [(d[0], [int(c) for c in d[1:]]) for d in data]

"""
      bul -- bur
      / :    /:
    ful -- fur:
     | bll  |blr
     |;     |;
    fll -- flr
    
    ^ /
    zy
     x>
"""

# part 1

class Box:
    def __init__(self, limits):
        self.x_min = limits[0]
        self.x_max = limits[1]
        self.y_min = limits[2]
        self.y_max = limits[3]
        self.z_min = limits[4]
        self.z_max = limits[5]
        
        self.tuple = tuple(limits)
        
    def __hash__(self):
        return hash(self.tuple)
    
    def __repr__(self):
        return repr(self.tuple)

    @staticmethod
    def check_between(val, min_val, max_val):
        return val >= min_val and val <= max_val
    
    def contains(self, box):
        x = box.x_min >= self.x_min and box.x_max <= self.x_max
        y = box.y_min >= self.y_min and box.y_max <= self.y_max
        z = box.z_min >= self.z_min and box.z_max <= self.z_max
        return x and y and z
    
    def glue(self, box):
        limits = None
        
        if self.contains(box):
            return box
        
        if self.y_min == box.y_min and self.y_max == box.y_max and self.z_min == box.z_min and self.z_max == box.z_max:
            limits = None
            if self.x_max + 1 >= box.x_min and self.x_max + 1 <= box.x_max:
                limits = (self.x_min, box.x_max, self.y_min, self.y_max, self.z_min, self.z_max)
            elif box.x_max + 1 >= self.x_min and box.x_max + 1 <= self.x_max:
                limits = (box.x_min, self.x_max, self.y_min, self.y_max, self.z_min, self.z_max)
               
        if self.x_min == box.x_min and self.x_max == box.x_max and self.z_min == box.z_min and self.z_max == box.z_max:
            limits = None
            if self.y_max + 1 >= box.y_min and self.y_max + 1 <= box.y_max:
                limits = (self.x_min, self.x_max, self.y_min, box.y_max, self.z_min, self.z_max)
            elif box.y_max + 1 >= self.y_min and box.y_max + 1 <= self.y_max:
                limits = (self.x_min, self.x_max, box.y_min, self.y_max, self.z_min, self.z_max)
                
        if self.x_min == box.x_min and self.x_max == box.x_max and self.y_min == box.y_min and self.y_max == box.y_max:
            limits = None
            if self.z_max + 1 >= box.z_min and self.z_max + 1 <= box.z_max:
                limits = (self.x_min, self.x_max, self.y_min, self.y_max, self.z_min, box.z_max)
            elif box.z_max + 1 >= self.z_min and box.z_max + 1 <= self.z_max:
                limits = (self.x_min, self.x_max, self.y_min, self.y_max, box.z_min, self.z_max)
        
        if limits is not None:
            return Box(limits)
        
        return None
        
    # front lower left    
    @property
    def fll(self):
        return (self.x_min,self.y_min,self.z_min)
    # front upper left
    @property
    def ful(self):
        return (self.x_min,self.y_min,self.z_max)
    # front lower right
    @property
    def flr(self):
        return (self.x_max,self.y_min,self.z_min)
    # front upper right
    @property
    def fur(self):
        return (self.x_max,self.y_min,self.z_max)        
    # back lower left
    @property
    def bll(self):
        return (self.x_min,self.y_max,self.z_min)
    # back upper left
    @property
    def bul(self):
        return (self.x_min,self.y_max,self.z_max)
    # back lower right
    @property
    def blr(self):
        return (self.x_max,self.y_max,self.z_min)
    # back upper right
    @property
    def bur(self):
        return (self.x_max,self.y_max,self.z_max)        
    
    def edges(self):
        edges = [[], [], []]
        edges[0].append((self.fll, self.flr))
        edges[0].append((self.bll, self.blr))
        edges[0].append((self.ful, self.fur))
        edges[0].append((self.bul, self.bur))
        
        edges[1].append((self.fll, self.bll))
        edges[1].append((self.flr, self.blr))
        edges[1].append((self.fur, self.bur))
        edges[1].append((self.ful, self.bul))
        
        edges[2].append((self.fll, self.ful))
        edges[2].append((self.flr, self.fur))
        edges[2].append((self.blr, self.bur))
        edges[2].append((self.bll, self.bul))
        
        return edges
    
    
    def cut_line(self, line, ax):
        def get_nodes(l0, l1, c0, c1):
            bounds = [(l0, -1), (l1, 1), (c0-1,1), (c0, -1), (c1,1), (c1+1, -1)]
            bounds = [b for b in bounds if b[0] >= l0 and b[0] <= l1]
            bounds = sorted(set(bounds))
            nodes = [(bounds[i][0], bounds[i+1][0]) for i in range(0, len(bounds), 2)]
            return tuple(nodes)
        
        if line[0][0] == line[1][0] and line[0][1] == line[1][1] and ax == 2:      
            nodes = get_nodes(line[0][2], line[1][2], self.z_min, self.z_max)
            return (line[0][0], line[0][1], nodes)
        elif line[0][0] == line[1][0] and line[0][2] == line[1][2] and ax == 1:
            nodes = get_nodes(line[0][1], line[1][1], self.y_min, self.y_max)
            return (line[0][0], nodes, line[0][2])
        elif line[0][1] == line[1][1] and line[0][2] == line[1][2] and ax == 0:
            nodes = get_nodes(line[0][0], line[1][0], self.x_min, self.x_max)
            return (nodes, line[0][1], line[0][2])
        
        
    
    def get_slices(self, box):
        div = [[], [], []]
        
        slices = set()
        
        
        for ax, edges in enumerate(self.edges()):
            d = set()
            for e in edges:
                cut = box.cut_line(e, ax)
                d.add(cut[ax])
            if len(d) > 1:
                raise ValueError()
            div[ax] = d.pop()                 
                
        for x_lim in div[0]:        
            for y_lim in div[1]:     
                for z_lim in div[2]:
                    limits = (x_lim[0], x_lim[1], y_lim[0], y_lim[1], z_lim[0], z_lim[1])
                    slices.add(Box(limits))
                                                    
        return slices
    
    def merge(self, box):
        result = self.cut(box)                
        result.add(box)
        return result
    
    @staticmethod
    def minimize(boxes):
        n_prev = len(boxes)
        while True:
            pop = None
            for b1 in boxes:
                for b2 in boxes:
                    if b1 is not b2:
                        g = b1.glue(b2)
                        if g is not None:
                            pop = (b1, b2, g)
                            break
                if pop is not None:
                    break
            if pop is not None:
                boxes.remove(pop[0])
                boxes.remove(pop[1])
                boxes.add(pop[2])
                            
            if n_prev == len(boxes):
                break
            n_prev = len(boxes)
        return boxes
    
    def cut(self, box):               
        slices = self.get_slices(box)       
        result = set()
                    
        for b in slices:
            if not box.contains(b):
                result.add(b) 
        
                
        return box.minimize(result)
    
    def volume(self, limit=None):        
        dx = self.x_max - self.x_min + 1
        dy = self.y_max - self.y_min + 1
        dz = self.z_max - self.z_min + 1
        
        if limit is not None and len(limit) == 2: 
            l0 = limit[0]
            l1 = limit[1]
            
            dx = min(self.x_max, l1) - max(self.x_min, l0) + 1
            if self.x_max < l0 or self.x_min > l1:
                dx = 0
            dy = min(self.y_max, l1) - max(self.y_min, l0) + 1
            if self.y_max < l0 or self.y_min > l1:
                dy = 0
            dz = min(self.z_max, l1) - max(self.z_min, l0) + 1
            if self.z_max < l0 or self.z_min > l1:
                dz = 0
            
        return dx * dy * dz
    
    def in_range(self, v_min, v_max):
        if self.x_max < v_min or self.x_min > v_max:
            return False
        if self.y_max < v_min or self.y_min > v_max:
            return False
        if self.z_max < v_min or self.z_min > v_max:
            return False
        return True
        
        
boxes = [(Box(rule[1]), rule[0] == 'on') for rule in data]

boxes_1 = [b for b in boxes if b[0].in_range(-50, 50)]

def blink(boxes):    
    lights = set([boxes[0][0]])
   
    for i in range(1, len(boxes)):
        box = boxes[i][0]
        is_on = boxes[i][1]
        
        new_light = set()
        for light in lights:
            cuts = light.cut(box)
            new_light = new_light.union(cuts)
        if is_on:
            new_light.add(box)
        lights = new_light
            
    return sum([b.volume() for b in lights])

tot = blink(boxes_1)
print(tot)

# part 2

boxes_2 = boxes
tot = blink(boxes_2)
print(tot)