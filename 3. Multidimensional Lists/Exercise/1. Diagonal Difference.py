def matrix_reader():
    row_count = int(input())
    the_matrix = []
    for row in range(row_count):
        col = list(map(int, input().split()))
        the_matrix.append(col)
    return the_matrix


def primary_diagonals_sum(the_matrix):
    primary_diagonal = 0
    for row in range(len(the_matrix)):
        primary_diagonal += the_matrix[row][row]
    return primary_diagonal


def secondary_diagonals_sum(the_matrix):
    secondary_diagonal = 0
    for row in range(len(the_matrix)):
        for col in range(row + 1, row + 2):
            secondary_diagonal += the_matrix[row][-col]
    return secondary_diagonal


matrix = matrix_reader()
result = abs(primary_diagonals_sum(matrix) - secondary_diagonals_sum(matrix))
print(result)
