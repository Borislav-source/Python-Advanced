def board_generator():
    board = [input().split() for _ in range(8)]
    return board


def locate_king(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != 'K':
                continue
            return r, c


def check_vertically_up(board, row, col, inner_list):
    for r in range(row, 0, -1):
        if board[r][col] != 'Q':
            continue
        inner_list.append([col, r])
        return


def check_vertically_down(board, row, col, inner_list):
    for r in range(row, len(board)):
        if board[r][col] != 'Q':
            continue
        inner_list.append([col, r])
        return


def check_horizontal_left(board, row, col, inner_list):
    for c in range(col, 0, -1):
        if board[row][c] != 'Q':
            continue
        inner_list.append([c, row])
        return


def check_horizontal_right(board, row, col, inner_list):
    for c in range(col, len(board[row])):
        if board[row][c] != 'Q':
            continue
        inner_list.append([c, row])
        return


def check_diagonal_up_left(board, row, col, inner_list):
    pass


def check_diagonal_up_right(board, row, col, inner_list):
    pass


def check_diagonal_down_left(board, row, col, inner_list):
    pass


def check_diagonal_down_right(board, row, col, inner_list):
    pass


list_of_queens = []
game_board = board_generator()
king_row, king_col = locate_king(game_board)
check_vertically_up(game_board, king_row, king_col, list_of_queens)
check_vertically_down(game_board, king_row, king_col, list_of_queens)
check_horizontal_left(game_board, king_row, king_col, list_of_queens)
check_horizontal_right(game_board, king_row, king_col, list_of_queens)
print(list_of_queens)
