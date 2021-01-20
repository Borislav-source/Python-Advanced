rows_count, columns_count = list(map(int, input().split()))


def matrix_generator(rows, columns, txt):
    the_matrix = []
    for r in range(rows):
        column = []
        for c in range(columns):
            if len(txt) >= columns:
                column.append(txt[c])
            else:
                for ch in range(len(txt)):
                    if len(column) < columns:
                        column.append(txt[ch])
        the_matrix.append(column)
        if columns < len(txt) or not columns % len(txt) == 0:
            difference = len(txt) - columns
            last = txt[-difference:]
            txt.clear()
            for j in range(len(last)):
                txt.append(last[j])
            for i in range(len(column)):
                txt.append(column[i])
    return the_matrix


text = [ch for ch in input()]
matrix = matrix_generator(rows_count, columns_count, text)

for row in range(len(matrix)):
    result = ''
    if not row % 2 == 0:
        matrix[row] = matrix[row][::-1]
    for col in range(len(matrix[row])):
        result += matrix[row][col]
    print(result)
