filename = "./d3data"


grid = []

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    grid.append(list(line.strip()))


def is_gear(x, y):
    seen = set()
    num_of_nums = 0
    num1 = ""
    num2 = ""
    for offset in [(x, y) for x in range(-1, 2) for y in range(-1, 2)]:
        x_offset, y_offset = offset
        try:
            if (
                grid[y + y_offset][x + x_offset].isdigit()
                and (x + x_offset, y + y_offset) not in seen
            ):
                num_of_nums += 1
                seen.add((x + x_offset, y + y_offset))
                left = x + x_offset - 1
                if left < 0:
                    start = 0
                right = x + x_offset + 1
                if right > len(grid[y]) - 1:
                    end = len(grid[y]) - 1

                while left >= 0:
                    seen.add((left, y + y_offset))
                    if not grid[y + y_offset][left].isdigit():
                        start = left + 1
                        break
                    elif left == 0:
                        start = left
                        left -= 1
                    else:
                        left -= 1

                while right <= len(grid[y]) - 1:
                    seen.add((right, y + y_offset))
                    if not grid[y + y_offset][right].isdigit():
                        end = right - 1
                        break
                    elif right == len(grid[y]) - 1:
                        end = right
                        right += 1
                    else:
                        right += 1
                if num_of_nums == 1 and num1 == "":
                    for i in range(start, end + 1):
                        num1 += grid[y + y_offset][i]
                elif num_of_nums == 2 and num2 == "":
                    for i in range(start, end + 1):
                        num2 += grid[y + y_offset][i]
                else:
                    return ("", "", False)

        except IndexError:
            continue
    if num_of_nums == 2:
        return (num1, num2, True)
    else:
        return ("", "", False)


def main():
    total = 0
    for y in range(len(grid)):
        index = 0
        while index != len(grid[y]):
            if grid[y][index] == "*":
                num1, num2, isgear = is_gear(index, y)
                if isgear:
                    total += int(num1) * int(num2)
                index += 1
            else:
                index += 1

    print(total)


if __name__ == "__main__":
    main()
