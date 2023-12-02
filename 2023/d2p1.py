input = "./d2data"
with open(input) as file:
    lines = file.readlines()

num_balls = {"blue": 14, "red": 12, "green": 13}
total = 0


def game_is_possible(draws):
    for draw in draws:
        balls = draw.split(",")
        for ball in balls:
            num, color = ball.split()
            if int(num) > num_balls[color]:
                return False
    return True


for line in lines:
    game, entry = line.split(":")
    _, ID = game.split()
    ID = int(ID)
    draws = entry.split(";")
    if game_is_possible(draws):
        total += ID

print(total)
