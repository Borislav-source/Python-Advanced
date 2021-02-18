def matrix_reader():
    rows_count = int(input())
    the_matrix = [list(map(int, input().split())) for _ in range(rows_count)]
    return columns_diagonal_sum(the_matrix)


def columns_diagonal_sum(board):
    the_sum = 0
    for row in range(len(board)):
        the_sum += board[row][row]
    return the_sum


print(matrix_reader())
