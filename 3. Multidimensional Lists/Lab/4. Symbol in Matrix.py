def matrix_reader():
    rows_count = int(input())
    the_matrix = [list(input()) for _ in range(rows_count)]
    return find_symbol_in_matrix(the_matrix)


def find_symbol_in_matrix(board):
    special_symbol = input()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == special_symbol:
                print((row, col))
                return
    print(f"{special_symbol} does not occur in the matrix")


matrix_reader()
