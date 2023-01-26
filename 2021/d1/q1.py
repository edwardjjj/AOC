import sys


with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n')

depths = [int(line) for line in lines]
current = 0
next = 1
count = 0
while(True):
    if next >= len(depths):
        break
    diff = depths[next] - depths[current]
    if diff > 0:
        count += 1
    next += 1
    current += 1

print(count)
