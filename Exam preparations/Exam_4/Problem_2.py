def board_generator():
    rows_count = int(input())
    board = [list(input()) for _ in range(rows_count)]
    return board

#
# def commands_list():
#     commands = []
#     cmd = input()
#     while cmd:
#         commands.append(cmd)
#         cmd = input()
#     return commands


def find_snake(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'S':
                return row, col


def validate(board, row, col):
    if row in range(len(board)) \
            and col in range(len(board[row])):
        return True


def burrow_pass(board, row):
    for r in range(len(board)):
        for c in range(len(board[row])):
            if board[r][c] == 'B':
                return r, c


def play(board, srow, scol, commands, food):
    for command in commands:
        if command == 'up':
            if validate(board, srow-1, scol):
                board[srow][scol] = '.'
                srow -= 1
                if board[srow][scol] == 'B':
                    board[srow][scol] = '.'
                    srow, scol = burrow_pass(board, srow)
                elif board[srow][scol] == '*':
                    food += 1
                board[srow][scol] = 'S'
                if food == 10:
                    return board, food
            else:
                board[srow][scol] = '.'
                return board, food
        elif command == 'down':
            if validate(board, srow+1, scol):
                board[srow][scol] = '.'
                srow += 1
                if board[srow][scol] == 'B':
                    board[srow][scol] = '.'
                    srow, scol = burrow_pass(board, srow)
                elif board[srow][scol] == '*':
                    food += 1
                board[srow][scol] = 'S'
                if food == 10:
                    return board, food
            else:
                board[srow][scol] = '.'
                return board, food
        elif command == 'left':
            if validate(board, srow, scol-1):
                board[srow][scol] = '.'
                scol -= 1
                if board[srow][scol] == 'B':
                    board[srow][scol] = '.'
                    srow, scol = burrow_pass(board, srow)
                elif board[srow][scol] == '*':
                    food += 1
                board[srow][scol] = 'S'
                if food == 10:
                    return board, food
            else:
                board[srow][scol] = '.'
                return board, food
        elif command == 'right':
            if validate(board, srow, scol+1):
                board[srow][scol] = '.'
                scol += 1
                if board[srow][scol] == 'B':
                    board[srow][scol] = '.'
                    srow, scol = burrow_pass(board, srow)
                elif board[srow][scol] == '*':
                    food += 1
                board[srow][scol] = 'S'
                if food == 10:
                    return board, food
            else:
                board[srow][scol] = '.'
                return board, food
    return board, food


def printing_results(board, food):
    if food == 10:
        print("You won! You fed the snake.")
    else:
        print("Game over!")
    print(f"Food eaten: {food}")
    for row in range(len(board)):
        print(*board[row], sep='')


eaten_food = 0
matrix = board_generator()
list_of_commands = []
cmd = input()
while cmd:
    list_of_commands.append(cmd)
    cmd = input()
s_row, s_col = find_snake(matrix)
matrix, eaten_food = play(matrix, s_row, s_col, list_of_commands, eaten_food)
printing_results(matrix, eaten_food)