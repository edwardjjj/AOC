import sys
class Board:
    def __init__(self):
        self.dict = {}
        self.row_states = [0] * 5
        self.column_states = [0] * 5
        self.value = 0

with open(sys.argv[1]) as file:
    lines = file.read().split('\n\n')

numbers = lines[0].split(',')
boards = []
states = []
for i in range(1, len(lines)): 
    input = lines[i].split('\n')
    current_board = Board()
    for row, line in enumerate(input):
        for column, char in enumerate(line.split()):
            current_board.dict[char] = (row, column)
            current_board.value += int(char)
    boards.append(current_board)

index = 0
max_state = 0
while(True):
    if len(boards) == 0:
        break
    if index == len(numbers):
        break
    number = numbers[index]
    boards_ = boards.copy()
    for board_index, board in enumerate(boards_):
        if number in board.dict:
            row, column = board.dict[number]
            board.row_states[row] += 1
            board.column_states[column] += 1
            board.value -= int(number)
            board_state = max(max(board.row_states),max(board.column_states))
            if board_state == 5:
                print(board.value * int(number))
                boards.remove(board)
    index += 1




    

