def matrix_reader():
    rows_count = int(input())
    the_matrix = [list(map(int, input().split())) for row in range(rows_count)]
    return the_matrix


matrix = matrix_reader()
data = input()
while not data == 'END':
    command = data.split()[0]
    row, col, value = list(map(int, data.split()[1:4]))
    if row in range(len(matrix)) and col in range(len(matrix[row])) and row >= 0 and col >= 0:
        if command == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    data = input()
[print(*row) for row in matrix]
