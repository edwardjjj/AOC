filename = './d3data'

grid = []

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    grid.append(list(line.strip()))

def is_part(index, y):

    end = 0
    for j in range(1, len(grid[y]) - index):
        if not grid[y][index + j].isdigit():
            end = j
            break
    if end == 0:
        end = len(grid[y]) - index

    ispart = False
    num = ''
    for x in range(end):
        for offset in [(x, y) for x in range(-1,2) for y in range(-1, 2)]:
            x_offset, y_offset = offset
            try:
                test = grid[y+y_offset][index+x+x_offset]
                if not test.isdigit() and test != '.':
                    ispart = True
            except IndexError:
                continue
        num = num + grid[y][index + x]
    return (num,end,ispart)

def main():


    total = 0
    for y in range(len(grid)):
        index = 0
        while index != len(grid[y]):
            if grid[y][index].isdigit():
                num, end, ispart = is_part(index, y)
                if ispart:
                    total += int(num)

                index += end
            else:
                index += 1


    print(total)

if __name__ == '__main__':
    main()
