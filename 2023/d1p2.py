input = "./d1data"
word_list = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}
with open(input) as file:
    lines = file.readlines()

total = 0
for line in lines:
    first_idx = len(line)
    last_idx = 0
    for word in list(word_list.keys()):
        idx = line.find(word)
        if idx != -1:
            if idx <= first_idx:
                first_digit = word_list[word]
                first_idx = idx
    for word in list(word_list.keys()):
        idx = line.rfind(word)
        if idx != -1:
            if idx >= last_idx:
                last_digit = word_list[word]
                last_idx = idx
    print(first_digit)
    # print(last_digit)
    total += int(str(first_digit) + str(last_digit))

print(total)
