import sys


with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n')


pos = 0
moves = {'forward': 1, 'up': -1j, 'down': 1j}
for line in lines:
    operation, distance = line.split(' ')
    pos += moves[operation] * int(distance)

result = pos.imag * pos.real

print(result)
