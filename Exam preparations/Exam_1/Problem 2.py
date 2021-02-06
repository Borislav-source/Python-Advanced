def matrix_constructor():
    rows_count = int(input())
    the_matrix = [list(input()) for _ in range(rows_count)]
    return the_matrix


def player_position(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'P':
                return row, col


def validate_move(com, board, choice):
    if com == 'up' or com == 'down':
        return choice in range(len(board))
    else:
        return choice in range(len(board[0]))


def move_up_or_down(com, choice, col, board, my_list):
    if not board[choice][col] == '-':
        my_list.append(board[choice][col])
    board[choice][col] = 'P'
    return choice, col


def move_left_or_right(com, choice, row, board, my_list):
    if not board[row][choice] == '-':
        my_list.append(board[row][choice])
    board[row][choice] = 'P'
    return row, choice


def play(com, board, my_list, row, col):
    mapper = {
        'up': -1,
        'down': +1,
        'left': -1,
        'right': +1
    }
    if com == 'up' or com == 'down':
        choice = row + mapper[com]
        if validate_move(com, board, choice):
            board[row][col] = '-'
            row, col = move_up_or_down(com, choice, col, board, my_list)
        else:
            if my_list:
                my_list.pop()
    elif com == 'left' or com == 'right':
        choice = col + mapper[com]
        if validate_move(com, board, choice):
            board[row][col] = '-'
            row, col = move_left_or_right(com, choice, row, board, my_list)
        else:
            if my_list:
                my_list.pop()
    return row, col, my_list


def print_result(board, msg):
    print(''.join(msg))
    for row in range(len(board)):
        print(*board[row], sep='')


message = list(input())
matrix = matrix_constructor()
commands_count = int(input())
s_row, s_col = player_position(matrix)
for _ in range(commands_count):
    command = input()
    s_row, s_col, letters = play(command, matrix, message, s_row, s_col)
print_result(matrix, message)
