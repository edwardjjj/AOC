import sys
import numpy as np


with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n')

bits = []
for line in lines:
    bits.append([int(x) for x in line])
bits = np.asarray(bits)

gamma = 0
epsilon = 0
for column in range(bits.shape[1]):
    g = np.bincount(bits[:,column]).argmax()
    gamma = (gamma << 1) + g
    epsilon = (epsilon << 1) + (1 - g)

print(gamma * epsilon)
