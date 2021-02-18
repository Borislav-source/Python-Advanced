def matrix_reader():
    rows_count, columns_count = list(map(int, input().split(', ')))
    the_matrix = [list(map(int, input().split())) for _ in range(rows_count)]
    return columns_sum(the_matrix, columns_count)


def columns_sum(board, col):
    for column in range(col):
        the_sum = 0
        for row in range(len(board)):
            the_sum += board[row][column]
        print(the_sum)
    return


matrix_reader()
