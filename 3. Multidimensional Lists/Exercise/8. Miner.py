def matrix_generator(rows):

    the_matrix = [input().split() for _ in range(rows)]
    return the_matrix


rows_count = int(input())
commands = input().split()
matrix = matrix_generator(rows_count)
current_row = 0
current_col = 0
number_of_coals = 0
game_over = False
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 's':
            current_row = row
            current_col = col
        elif matrix[row][col] == 'c':
            number_of_coals += 1
for command in commands:
    if command == 'up':
        if current_row - 1 in range(len(matrix)):
            current_row -= 1
    elif command == 'down':
        if current_row + 1 in range(len(matrix)):
            current_row += 1
    elif command == 'right':
        if current_col + 1 in range(len(matrix[current_row])):
            current_col += 1
    elif command == 'left':
        if current_col - 1 in range(len(matrix[current_row])):
            current_col -= 1

    if matrix[current_row][current_col] == 'c':
        number_of_coals -= 1
        matrix[current_row][current_col] = '*'
        if number_of_coals == 0:
            print(f"You collected all coals! ({current_row}, {current_col})")
    elif matrix[current_row][current_col] == 'e':
        if number_of_coals:
            print(f"Game over! ({current_row}, {current_col})")
            game_over = True
            break
if number_of_coals and not game_over:
    print(f"{number_of_coals} coals left. ({current_row}, {current_col})")


