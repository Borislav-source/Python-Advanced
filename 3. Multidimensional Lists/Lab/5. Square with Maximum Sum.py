def matrix_reader():
    rows_count, columns_count = list(map(int, input().split(', ')))
    the_matrix = [list(map(int, input().split(', '))) for _ in range(rows_count)]
    return sub_matrix_sum(the_matrix)


def sub_matrix_sum(board):
    the_sum = 0
    element = ()
    for row in range(len(board)-1):
        for col in range(len(board[row])-1):
            sub_sum = 0
            for el in range(col, col+2):
                sub_sum += board[row][el]
                sub_sum += board[row+1][el]
            if sub_sum > the_sum:
                the_sum = sub_sum
                element = row, col
    row, col = element
    for r in range(row, row + 2):
        print(board[r][col], board[r][col+1])
    print(the_sum)
    return


result = matrix_reader()
