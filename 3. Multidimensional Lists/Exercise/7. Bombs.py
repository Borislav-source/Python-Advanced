def matrix_reader():
    the_matrix = [list(map(int, input().split())) for row in range(int(input()))]
    return the_matrix


matrix = matrix_reader()
bomb_coordinates = input().split()
bomb_coordinates = [list(map(int, el.split(','))) for el in bomb_coordinates]
blown = []
for cord in bomb_coordinates:
    row = cord[0]
    col = cord[1]
    bomb = matrix[row][col]
    size = 2
    for i in range(-1, size):
        if row + i in range(len(matrix)):
            for c in range(-1, 2):
                if col + c in range(len(matrix[row])):
                    if not [row+i, col+c] in bomb_coordinates and not [row+i, col+c] in blown:
                        matrix[row+i][col+c] -= bomb
                        if matrix[row+i][col+c] <= 0:
                            current = [row+i, col+c]
                            blown.append(current)
    matrix[row][col] = 0
    current = [row, col]
    blown.append(current)
alive_cells = [matrix[r][el] for r in range(len(matrix)) for el in range(len(matrix[r])) if matrix[r][el] > 0]
print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
for r in range(len(matrix)):
    print(*matrix[r])
