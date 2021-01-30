from sys import maxsize

def matrix_reader():
    rows_count, columns_count = list(map(int, input().split()))
    the_matrix = []
    for row in range(rows_count):
        the_matrix.append(list(map(int, input().split())))
    return the_matrix


def find_biggest_sum(the_matrix, sub_matrix_size):
    global starts_from
    best_sum = -maxsize
    for row in range(len(the_matrix) - 2):
        for col in range(len(the_matrix[row]) - 2):
            current_sum = 0
            for n in range(row, row + sub_matrix_size):
                for i in range(col, col + sub_matrix_size):
                    current_sum += matrix[n][i]
            if current_sum > best_sum:
                best_sum = current_sum
                starts_from = [row, col, best_sum]
    return starts_from


matrix = matrix_reader()
size = 3
row, col, best = find_biggest_sum(matrix, size)
print(f'Sum = {best}')
for r in range(row, row + size):
    column = []
    for c in range(col, col + size):
        column.append(matrix[r][c])
    print(*column)
