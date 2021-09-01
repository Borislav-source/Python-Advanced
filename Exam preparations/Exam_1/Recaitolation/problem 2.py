def load_matrix(rows):
    mtrx = []
    for r in range(rows):
        c = list(input())
        mtrx.append(c)
    return mtrx


def commands_loader(count):
    commands = []
    for com in range(count):
        command = input()
        commands.append(command)
    return commands


def find_player_on_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'P':
                return row, col


def validate_move(board, row, col):
    if row in range(len(board)) and col in range(len(board[row])):
        return True
    return False


def move(in_str, board, row, col):
    if board[row][col] != '-':
        in_str += board[row][col]
    board[row][col] = 'P'
    return in_str, board


initial_string = input()
n = int(input())

matrix = load_matrix(n)

commands_count = int(input())

commands = commands_loader(commands_count)
p_row, p_col = find_player_on_board(matrix)

for command in commands:
    if command == 'up':
        if validate_move(matrix, p_row - 1, p_col):
            matrix[p_row][p_col] = '-'
            p_row -= 1
            initial_string, matrix = move(initial_string, matrix, p_row, p_col)
        else:
            initial_string = initial_string[:-1]
    elif command == 'down':
        if validate_move(matrix, p_row + 1, p_col):
            matrix[p_row][p_col] = '-'
            p_row += 1
            initial_string, matrix = move(initial_string, matrix, p_row, p_col)
        else:
            initial_string = initial_string[:-1]
    elif command == 'left':
        if validate_move(matrix, p_row, p_col - 1):
            matrix[p_row][p_col] = '-'
            p_col -= 1
            initial_string, matrix = move(initial_string, matrix, p_row, p_col)
        else:
            initial_string = initial_string[:-1]
    elif command == 'right':
        if validate_move(matrix, p_row, p_col + 1):
            matrix[p_row][p_col] = '-'
            p_col += 1
            initial_string, matrix = move(initial_string, matrix, p_row, p_col)
        else:
            initial_string = initial_string[:-1]

print(initial_string)
for r in range(len(matrix)):
    print(*matrix[r], sep='')

