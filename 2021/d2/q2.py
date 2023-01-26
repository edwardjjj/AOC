import sys


with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n')

aim = 0
pos = 0
moves = {'forward': 1, 'up': -1j, 'down': 1j}
for line in lines:
    operation, distance = line.split(' ')
    if operation == 'forward':
        pos += int(distance) * moves[operation] + int(distance) * aim
    else:
        aim += moves[operation] * int(distance) 

result = pos.imag * pos.real

print(result)
