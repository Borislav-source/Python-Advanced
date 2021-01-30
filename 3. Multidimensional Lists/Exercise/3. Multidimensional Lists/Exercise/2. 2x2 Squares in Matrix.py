def matrix_reader():
    (rows_count, columns_count) = list(map(int, input().split()))
    the_matrix = []
    for row in range(rows_count):
        the_matrix.append(input().split())
    return the_matrix


def find_pattern(the_matrix):
    counter = 0
    for r in range(len(the_matrix) - 1):
        for c in range(len(the_matrix[r]) - 1):
            if the_matrix[r][c] == the_matrix[r][c+1]:
                if the_matrix[r+1][c] == the_matrix[r+1][c+1] == the_matrix[r][c]:
                    counter += 1
    return counter


matrix = matrix_reader()
print(find_pattern(matrix))