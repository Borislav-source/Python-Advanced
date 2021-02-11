def board_generator():
    board = [list(input()) for _ in range(int(input()))]
    return find_snake(board)


def find_snake(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'S':
                return play(board, row, col, food=0)


def validate(board, row, col):
    if row in range(len(board)) \
            and col in range(len(board[row])):
        return True


def burrow_pass(board, row):
    for r in range(len(board)):
        for c in range(len(board[row])):
            if board[r][c] == 'B':
                return r, c


def play(board, srow, scol, food):
    while True:
        command = input()
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
                if food >= 10:
                    return printing_results(board, food)
            else:
                board[srow][scol] = '.'
                return printing_results(board, food)
        if command == 'down':
            if validate(board, srow+1, scol):
                board[srow][scol] = '.'
                srow += 1
                if board[srow][scol] == 'B':
                    board[srow][scol] = '.'
                    srow, scol = burrow_pass(board, srow)
                elif board[srow][scol] == '*':
                    food += 1
                board[srow][scol] = 'S'
                if food >= 10:
                    return printing_results(board, food)
            else:
                board[srow][scol] = '.'
                return printing_results(board, food)
        if command == 'left':
            if validate(board, srow, scol-1):
                board[srow][scol] = '.'
                scol -= 1
                if board[srow][scol] == 'B':
                    board[srow][scol] = '.'
                    srow, scol = burrow_pass(board, srow)
                elif board[srow][scol] == '*':
                    food += 1
                board[srow][scol] = 'S'
                if food >= 10:
                    return printing_results(board, food)
            else:
                board[srow][scol] = '.'
                return printing_results(board, food)
        if command == 'right':
            if validate(board, srow, scol+1):
                board[srow][scol] = '.'
                scol += 1
                if board[srow][scol] == 'B':
                    board[srow][scol] = '.'
                    srow, scol = burrow_pass(board, srow)
                elif board[srow][scol] == '*':
                    food += 1
                board[srow][scol] = 'S'
                if food >= 10:
                    return printing_results(board, food)
            else:
                board[srow][scol] = '.'
                return printing_results(board, food)


def printing_results(board, food):
    if food == 10:
        print("You won! You fed the snake.")
    else:
        print("Game over!")
    print(f"Food eaten: {food}")
    for row in range(len(board)):
        print(*board[row], sep='')


board_generator()
