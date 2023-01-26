import sys
WINDOW_SIZE = 3

with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n')

depths = [int(line) for line in lines]
count = 0
current = 0
while(True):
    if (current + WINDOW_SIZE) >= len(depths):
        break
    current_window = sum(depths[current + x] for x in range(WINDOW_SIZE))
    next_window = sum(depths[current + x + 1] for x in range(WINDOW_SIZE))
    diff = next_window - current_window
    if diff > 0:
        count += 1
    current += 1

print(count)
