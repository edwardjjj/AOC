def main():
    filename = "./d4data"
    with open(filename) as file:
        lines = file.readlines()

    total = 0

    for line in lines:
        _, input = line.strip().split(":")
        num_win, num_own = input.split("|")
        num_win = set(map(int, num_win.split()))
        num_own = list(map(int, num_own.split()))
        count = 0
        for num in num_own:
            if num in num_win:
                count += 1
        if count >= 1:
            total += 2 ** (count - 1)
    print(total)


if __name__ == "__main__":
    main()
