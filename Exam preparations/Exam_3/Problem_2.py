def board_generator():
    rows_count = int(input())
    cols_count = rows_count
    the_matrix = []
    for row in range(rows_count):
        column = []
        for col in range(cols_count):
            column.append(1)
        the_matrix.append(column)
    return the_matrix


def put_the_bombs(board):
    bombs_count = int(input())
    for b in range(bombs_count):
        row, col = input().strip('()').split(', ')
        board[int(row)][int(col)] = '*'
    return board


def fill_the_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            counter = 0
            if board[row][col] is not '*':
                counter = check_for_bombs(board, row, col, counter)
                board[row][col] = counter
    return board


def check_for_bombs(board, row, col, count=0):
    if row-1 in range(len(board)):
        if col-1 in range(len(board[row])):
            if board[row-1][col-1] == '*':
                count += 1
        if board[row-1][col] == '*':
            count += 1
        if col+1 in range(len(board[row])):
            if board[row-1][col+1] == '*':
                count += 1
    if row+1 in range(len(board)):
        if col-1 in range(len(board[row])):
            if board[row+1][col-1] == '*':
                count += 1
        if board[row+1][col] == '*':
            count += 1
        if col+1 in range(len(board[row])):
            if board[row+1][col+1] == '*':
                count += 1
    if col-1 in range(len(board)):
        if board[row][col - 1] == '*':
            count += 1
    if col+1 in range(len(board)):
        if board[row][col + 1] == '*':
            count += 1

    return count


def printing_result(board):
    for row in range(len(board)):
        print(*board[row], sep=' ')


matrix = board_generator()
put_the_bombs(matrix)
printing_result(fill_the_board(matrix))