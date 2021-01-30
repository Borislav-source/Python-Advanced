def matrix_reader ():
    (row_count, column_count) = map(int, input().split(', '))
    matrix = []
    for r in range(row_count):
        row = list(map(int, input(). split(', ')))
        matrix.append(row)
    return matrix


matrix = matrix_reader()
the_sum = 0
for r in matrix:
    for el in range(len(r)):
        the_sum += r[el]
print(the_sum)
print(matrix)