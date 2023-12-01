input = "./d1data"
with open(input) as file:
    lines = file.readlines()

digits = []
total = 0
for line in lines:
    digits_inline = []
    for char in line:
        try:
            num = int(char)
            digits_inline.append(num)
        except ValueError:
            continue
    digits.append(digits_inline)
    total += int(str(digits_inline[0]) + str(digits_inline[-1]))

print(total)
