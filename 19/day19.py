#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:58:39 2021

"""

with open('input.txt', mode='r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    scanners = []
    s = []
    
    for l in lines:
        if l[0:3] == '---':
            s = []
        elif len(l) == 0:
            scanners.append(s)
        else:
            s.append(tuple(int(c) for c in l.split(',')))
            
    scanners.append(s)         
    
# part 1
    
def add(t1, t2):
    return tuple(e1+e2 for e1, e2 in zip(t1, t2))

def diff(t1, t2):
    return tuple(e1-e2 for e1, e2 in zip(t1, t2))

def mul(a, v):
    return tuple(sum([a[i][j]*v[j] for j in range(len(v))]) for i in range(len(a)))

rot90 = {
    'x': ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
    'y': ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
    'z': ((0, -1, 0), (1, 0, 0), (0, 0, 1))
}

def get_rotations(v):
    # thanks https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
    def rot(v, axes = []):
        axes.reverse()
        for a in axes:
            v = mul(rot90[a], v)
        return v
    
    result = [rot(v)]
    rotations = ['x', 'y', 'z', 
                 'xx', 'xy', 'xz', 'yx', 'yy', 'zy', 'zz', 
                 'xxx', 'xxy', 'xxz', 'xyx', 'xyy', 'xzz', 'yxx', 'yyy', 'zzz',
                 'xxxy', 'xxyx', 'xyxx', 'xyyy']
    result.extend([rot(v, list(r)) for r in rotations])
    
    return result

def rotate_list(vec_list):
    rotated = []
    for v in vec_list:
        rotated.append(get_rotations(v))
    
    return [[rotated[i][j] for i in range(len(vec_list))] for j in range(24)]

def flatten(arr2d):
    r = []
    for arr in arr2d:
        r.extend(arr)
    return r

def correlate(reference, points):
    diffs = {}
    for r in reference:
        for p in points:
            d = diff(r, p)
            if d in diffs:
                diffs[d] += 1
            else:
                diffs[d] = 1
    
    candidates = sorted([(d, diffs[d]) for d in diffs if diffs[d] > 1], key=lambda c: c[1], reverse=True)
    return len(candidates) > 0, candidates


def match(reference, scanners, matches):
    unmatched = []
    for s_i, s in enumerate(scanners):
        rotations = rotate_list(s)
        candidates = []
        found = False
        for i, points in enumerate(rotations):
            c = correlate(reference, points)
            if c[0]:
                candidates.append((c[1][0], i))
                
        if len(candidates) > 0:
            found = True
            candidates.sort(key=lambda c: c[0][1], reverse=True)
            winner = candidates[0]
            pos = winner[0][0]
            matches.append(pos)
            new_points = [add(pt, pos) for pt in rotations[winner[1]]]
            
            reference = reference.union(set(new_points))
                    
        if not found:
            unmatched.append(s)
        
    return reference, unmatched

reference = set(scanners[0])
unmatched = scanners[1:]
matches = [(0,0,0)]
while len(unmatched) > 0:
    reference, unmatched = match(reference, unmatched, matches)
    print("remaining", len(unmatched))

print(len(reference))

# part 2

def dist(t1, t2):
    return sum([abs(v) for v in diff(t2, t1)])

max_dist = 0

for m1 in matches:
    for m2 in matches:
        max_dist = max(max_dist, dist(m1, m2))
        
print(max_dist)