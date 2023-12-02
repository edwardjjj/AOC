input = "./d2data"
with open(input) as file:
    lines = file.readlines()

total = 0


for line in lines:
    game, entry = line.split(":")
    _, ID = game.split()
    ID = int(ID)
    draws = entry.split(";")
    nums = [0, 0, 0]
    for draw in draws:
        balls = draw.split(",")
        for ball in balls:
            num, color = ball.split()
            num = int(num)
            if color == "blue":
                if num > nums[0]:
                    nums[0] = num
            if color == "green":
                if num > nums[1]:
                    nums[1] = num
            if color == "red":
                if num > nums[2]:
                    nums[2] = num

    total += nums[0] * nums[1] * nums[2]
print(total)
