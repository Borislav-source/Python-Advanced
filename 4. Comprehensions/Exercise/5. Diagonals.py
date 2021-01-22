def matrix_reader():
    rows_count = int(input())
    the_matrix = [input().split(', ') for _ in range(rows_count)]
    return the_matrix


def parse(diagonal):
    return list(map(int, diagonal))


matrix = matrix_reader()
first_diagonal = [matrix[r][r] for r in range(len(matrix))]
second_diagonal = [matrix[r][-c] for r in range(len(matrix)) for c in range(r+1, r+2)]
print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum(parse(first_diagonal))}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum(parse(second_diagonal))}")
