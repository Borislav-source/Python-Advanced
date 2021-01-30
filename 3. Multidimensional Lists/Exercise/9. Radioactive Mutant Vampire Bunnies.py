def matrix_reader(rows):
    the_matrix = [list(input()) for _ in range(rows)]
    return the_matrix


def player_move(comnd, winning, loose, final_coordinates):
    for rows in range(rows_count):
        for cols in range(cols_count):
            if matrix[rows][cols] == 'P':
                if comnd == 'U':
                    if rows-1 in range(len(matrix)):
                        if matrix[rows-1][cols] is not 'B':
                            matrix[rows-1][cols] = 'P'
                        else:
                            final_coordinates = rows - 1, cols
                            loose = True
                        matrix[rows][cols] = '.'
                    else:
                        final_coordinates = rows, cols
                        winning = True
                        matrix[rows][cols] = '.'
                if comnd == 'D':
                    if rows+1 in range(len(matrix)):
                        if matrix[rows+1][cols] is not 'B':
                            matrix[rows+1][cols] = 'P'
                        else:
                            final_coordinates = rows + 1, cols
                            loose = True
                        matrix[rows][cols] = '.'
                    else:
                        final_coordinates = rows, cols
                        winning = True
                        matrix[rows][cols] = '.'
                if comnd == 'L':
                    if cols-1 in range(len(matrix)):
                        if matrix[rows][cols-1] is not 'B':
                            matrix[rows][cols-1] = 'P'
                        else:
                            final_coordinates = rows, cols-1
                            loose = True
                        matrix[rows][cols] = '.'
                    else:
                        final_coordinates = rows, cols
                        winning = True
                        matrix[rows][cols] = '.'
                if comnd == 'R':
                    if cols+1 in range(len(matrix)):
                        if matrix[rows][cols+1] is not 'B':
                            matrix[rows][cols+1] = 'P'
                        else:
                            final_coordinates = rows, cols+1
                            loose = True
                        matrix[rows][cols] = '.'
                    else:
                        final_coordinates = rows, cols
                        winning = True
                        matrix[rows][cols] = '.'
                return winning, loose, final_coordinates


def bunnies_spread(loose, winning, final_coordinates):
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == 'B':
                if row - 1 in range(len(matrix)):
                    if matrix[row - 1][col] == 'P':
                        matrix[row-1][col] = 'B'
                        loose = True
                        final_coordinates = row - 1, col
                    matrix[row - 1][col] = 'b'
                if row + 1 in range(len(matrix)):
                    if matrix[row + 1][col] == 'P':
                        matrix[row+1][col] = 'B'
                        loose = True
                        final_coordinates = row + 1, col
                    matrix[row + 1][col] = 'b'
                if col + 1 in range(cols_count):
                    if matrix[row][col + 1] == 'P':
                        matrix[row][col + 1] = 'B'
                        loose = True
                        final_coordinates = row, col + 1
                    matrix[row][col + 1] = 'b'
                if col - 1 in range(cols_count):
                    if matrix[row][col - 1] == 'P':
                        matrix[row][col - 1] = 'B'
                        loose = True
                        final_coordinates = row, col - 1
                    matrix[row][col - 1] = 'b'
    return winning, loose, final_coordinates


rows_count, cols_count = list(map(int, input().split()))
matrix = matrix_reader(rows_count)
# print(matrix)
commands = list(input())
lost = False
win = False
final_coordinates = ()


for command in commands:
    result = player_move(command, win, lost, final_coordinates)
    win, lost, final_coordinates = result
    result = bunnies_spread(lost, win, final_coordinates)
    win, lost, final_coordinates = result
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == 'b':
                matrix[row][col] = 'B'
    if win or lost:
        break

for r in matrix:
    print(''.join(r))

if win:
    print(f"won: {final_coordinates[0]} {final_coordinates[1]}")
else:
    print(f"dead: {final_coordinates[0]} {final_coordinates[1]}")



