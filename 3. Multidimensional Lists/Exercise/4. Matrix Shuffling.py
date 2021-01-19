rows_count, columns_count = list(map(int, input().split()))


def matrix_generator(rows):
    the_matrix = []
    for row in range(rows_count):
        column = input().split()
        the_matrix.append(column)
    return the_matrix


def swap(matrix, r1, r2, c1, c2):
    first_value = matrix[r1][c1]
    second_value = matrix[r2][c2]
    matrix[r1][c1] = second_value
    matrix[r2][c2] = first_value
    return matrix


matrix = matrix_generator(rows_count)
data = input()
while not data == 'END':
    data = data.split()
    if len(data) == 5:
        command = data[0]
        data.remove(data[0])
        row1, col1, row2, col2 = list(map(int, data))
        if command == 'swap':
            if row1 in range(rows_count) and row2 in range(rows_count):
                if col1 in range(columns_count) and col2 in range(columns_count):
                    matrix = swap(matrix, row1, row2, col1, col2)
                    for r in range(len(matrix)):
                        column = []
                        for c in range(len(matrix[r])):
                            column.append(matrix[r][c])
                        print(*column)
                    data = input()
                    continue
    print('Invalid input!')
    data = input()
