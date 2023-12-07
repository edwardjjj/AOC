def main():
    filename = "./d4data"
    # filename = "./d4test"
    with open(filename) as file:
        lines = file.readlines()

    num_cards = [1 for _ in range(len(lines))]
    for y, line in enumerate(lines):
        _, input = line.strip().split(":")
        num_win, num_own = input.split("|")
        num_win = set(map(int, num_win.split()))
        num_own = list(map(int, num_own.split()))
        count = 0
        for num in num_own:
            if num in num_win:
                count += 1
        if count >= 1:
            for i in range(y + 1, y + count + 1):
                if i >= len(num_cards):
                    continue
                num_cards[i] += num_cards[y]
    print(sum(num_cards))


if __name__ == "__main__":
    main()
