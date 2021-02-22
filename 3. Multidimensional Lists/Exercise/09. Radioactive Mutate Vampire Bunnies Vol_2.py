def matrix_reader():
    rows_count, cols_count = list(map(int, input().split()))
    the_matrix = [list(input()) for _ in range(rows_count)]
    return the_matrix


def find_the_player(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'P':
                return row, col


def validate_move(board, row, col):
    if row in range(len(board)) and \
            col in range(len(board[row])):
        return True
    else:
        return False


def play(board, moves, row, col, loose=False, final_coordinates=()):
    for move in moves:
        if not loose:
            board[row][col] = '.'
            if move == 'U':
                if validate_move(board, row-1, col):
                    row -= 1
                    if not board[row][col] == "B":
                        board[row][col] = 'P'
                    else:
                        loose = True
                else:
                    break
            elif move == 'D':
                if validate_move(board, row+1, col):
                    row += 1
                    if not board[row][col] == "B":
                        board[row][col] = 'P'
                    else:
                        loose = True
                else:
                    break
            elif move == 'L':
                if validate_move(board, row, col-1):
                    col -= 1
                    if not board[row][col] == "B":
                        board[row][col] = 'P'
                    else:
                        loose = True
                else:
                    break
            elif move == 'R':
                if validate_move(board, row, col+1):
                    col += 1
                    if not board[row][col] == "B":
                        board[row][col] = 'P'
                    else:
                        loose = True
                else:
                    break
            if not loose:
                board, loose, final_coordinates = bunnies_spread(board)
                if loose:
                    return board, loose, final_coordinates
        else:
            break
    final_coordinates = row, col
    board = bunnies_spread(board)[0]
    return board, loose, final_coordinates


def bunnies_spread(board, loose=False, final_coordinates=()):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'B':
                if validate_move(board, row-1, col):
                    if board[row - 1][col] == 'P':
                        board[row - 1][col] = 'B'
                        loose = True
                        final_coordinates = row - 1, col
                    board[row - 1][col] = 'b'
                if validate_move(board, row+1, col):
                    if board[row + 1][col] == 'P':
                        board[row + 1][col] = 'B'
                        loose = True
                        final_coordinates = row + 1, col
                    board[row + 1][col] = 'b'
                if validate_move(board, row, col+1):
                    if board[row][col + 1] == 'P':
                        board[row][col + 1] = 'B'
                        loose = True
                        final_coordinates = row, col + 1
                    board[row][col + 1] = 'b'
                if validate_move(board, row, col-1):
                    if board[row][col - 1] == 'P':
                        board[row][col - 1] = 'B'
                        loose = True
                        final_coordinates = row, col - 1
                    board[row][col - 1] = 'b'
    for row in range(len(board)):
        for col in range(len(board[row])):
            if matrix[row][col] == 'b':
                matrix[row][col] = 'B'
    return board, loose, final_coordinates


def printing_results(board, cond, coordinates):
    r, c = coordinates
    for row in range(len(board)):
        print(''.join(board[row]))
    if cond:
        print(f'dead: {r} {c}')
    else:
        print(f'won: {r} {c}')


matrix = matrix_reader()
list_of_moves = list(input())
player_row, player_col = find_the_player(matrix)
matrix, condition, last_coordinates = play(matrix, list_of_moves, player_row, player_col)
printing_results(matrix, condition, last_coordinates)