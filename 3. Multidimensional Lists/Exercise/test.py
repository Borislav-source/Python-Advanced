# def matrix_generator():
#     rows_count = int(input())
#     the_matrix = []
#     for row in range(rows_count):
#         line = input()
#         the_matrix.append(line)
#     return the_matrix
#
#
# matrix = matrix_generator()
# counter = 0
# for r in range(len(matrix)):
#     for el in range(len(matrix[r])):
#         if matrix[r][el] == 'K':
#             if r-2 in range(len(matrix)-1):
#                 if el-1 in range(len(matrix[r-2])-1):
#                     if matrix[r-2][el-1] == 'K':
#                         matrix[r-2] = matrix[r-2][:el-1] + '0' + matrix[r-2][el:]
#                         counter += 1
#                 if el+1 in range(len(matrix[r-2])-1):
#                     if matrix[r-2][el+1] == 'K':
#                         matrix[r-2] = matrix[r-2][:el+1] + '0' + matrix[r-2][el + 2:]
#                         counter += 1
#             if r+2 in range(len(matrix)-1):
#                 if el-1 in range(len(matrix[r + 2])-1):
#                     if matrix[r + 2][el - 1] == 'K':
#                         matrix[r+2] = matrix[r+2][:el-1] + '0' + matrix[r+2][el:]
#                         counter += 1
#                 if el+1 in range(len(matrix[r + 2])-1):
#                     if matrix[r + 2][el + 1] == 'K':
#                         matrix[r+2] = matrix[r+2][:el+1] + '0' + matrix[r+2][el + 2:]
#                         counter += 1
#             if r-1 in range(len(matrix)-1):
#                 if el-2 in range(len(matrix[r-1])-1):
#                     if matrix[r-1][el-2] == 'K':
#                         matrix[r-1] = matrix[r-1][:el-2] + '0' + matrix[r-1][el-1:]
#                         counter += 1
#                 if el+2 in range(len(matrix[r-1])-1):
#                     if matrix[r-1][el+2] == 'K':
#                         matrix[r-1] = matrix[r-1][:el+2] + '0' + matrix[r-1][el + 3:]
#                         counter += 1
#             if r+1 in range(len(matrix)-1):
#                 if el-2 in range(len(matrix[r+1])-1):
#                     if matrix[r+1][el-2] == 'K':
#                         matrix[r+1] = matrix[r+1][:el-2] + '0' + matrix[r+1][el-1:]
#                         counter += 1
#                 if el+2 in range(len(matrix[r+1])-1):
#                     if matrix[r+1][el+2] == 'K':
#                         matrix[r+1] = matrix[r+1][:el+2] + '0' + matrix[r+1][el + 3:]
#                         counter += 1
#
# print(counter)
#
#
# nums = []
# a = 5
# b = 6
# nums.append([a, b])
# print(nums)

# a = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ]
# a[1][0] += 1
# print(a)


# a = 2, 3
# print(a)


def play(board, moves, row, col, loose=False, final_coordinates=()):
    for move in moves:
        if not loose:
            board[row][col] = '.'
            if move == 'U':
                if validate_move(board, row-1, col):
                    if not board[row-1][col] == "B":
                        board[row-1][col] = 'P'
                        row -= 1
                    else:
                        loose = True
                else:
                    loose = True
            elif move == 'D':
                if validate_move(board, row+1, col):
                    if not board[row+1][col] == "B":
                        row += 1
                        board[row+1][col] = 'P'
                    else:
                        loose = True
                else:
                    loose = True
            elif move == 'L':
                if validate_move(board, row, col-1):
                    if not board[row][col-1] == "B":
                        board[row][col-1] = 'P'
                        col -= 1
                    else:
                        loose = True
                else:
                    loose = True
            elif move == 'R':
                if validate_move(board, row, col+1):
                    if not board[row][col+1] == "B":
                        board[row][col+1] = 'P'
                        col += 1
                    else:
                        loose = True
                else:
                    loose = True
            board, loose, final_coordinates = bunnies_spread(board)
        else:
            break
    return board, loose, final_coordinates

# for move in moves:
#
#     if not loose:


def play(board, moves, row, col, loose=False, final_coordinates=()):
    for move in moves:
        board, loose, final_coordinates = bunnies_spread(board)
        if not loose:
            board[row][col] = '.'
            final_coordinates = row, col
            if move == 'U':
                if validate_move(board, row-1, col):
                    if not board[row-1][col] == "B":
                        board[row-1][col] = 'P'
                        row -= 1
                    else:
                        break
                else:
                    break
            elif move == 'D':
                if validate_move(board, row+1, col):
                    if not board[row+1][col] == "B":
                        row += 1
                        board[row+1][col] = 'P'
                    else:
                        break
                else:
                    break
            elif move == 'L':
                if validate_move(board, row, col-1):
                    if not board[row][col-1] == "B":
                        board[row][col-1] = 'P'
                        col -= 1
                    else:
                        break
                else:
                    break
            elif move == 'R':
                if validate_move(board, row, col+1):
                    if not board[row][col+1] == "B":
                        board[row][col+1] = 'P'
                        col += 1
                    else:
                        break
                else:
                    break
        else:
            break
    return board, loose, final_coordinates