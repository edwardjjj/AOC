import sys
import numpy as np


with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n')

bits = []
for line in lines:
    bits.append([int(x) for x in line])
bits = np.array(bits)
o2 = np.copy(bits)
co2 = np.copy(bits)
column = 0
while(True):
    if o2.shape[0] == 1:
        break
    bin = np.bincount(o2[:,column])
    common_bit = 0
    if bin[1] > bin[0]:
        common_bit = 1
    if bin[1] < bin[0]:
        common_bit = 0
    if bin[1] == bin[0]:
        common_bit = 1
    indices = np.where(o2[:,column] == common_bit)
    o2 = o2[indices]
    column += 1

column = 0
while(True):
    if co2.shape[0] == 1:
        break
    bin = np.bincount(co2[:,column])
    common_bit = 0
    if bin[1] > bin[0]:
        common_bit = 0
    if bin[1] < bin[0]:
        common_bit = 1
    if bin[1] == bin[0]:
        common_bit = 0
    indices = np.where(co2[:,column] == common_bit)
    co2 = co2[indices]
    column += 1
o2_rating = 0
for digit in o2[0]:
    o2_rating = (o2_rating << 1) + digit

co2_rating = 0
for digit in co2[0]:
    co2_rating = (co2_rating << 1) + digit

print(o2_rating * co2_rating)
