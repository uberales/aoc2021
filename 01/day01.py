import numpy as np

with open('input.txt', mode='r') as f:
    data = np.array([int(l.strip()) for l in f.readlines()])

# part 1
differences = data[1:] - data[0:-1]
num_inc = sum(differences > 0)
print(num_inc)

# part 2
sums_3 = np.array([sum(data[i:i+3]) for i in range(len(data)-2)])
differences = sums_3[1:] - sums_3[0:-1]
num_inc = sum(differences > 0)
print(num_inc)