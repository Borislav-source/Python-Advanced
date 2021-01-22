# def matrix_generator(alpha):
#     rows_count, columns_count = list(map(int, input().split()))
#     the_matrix = []
#     for row in range(rows_count):
#         result = []
#         for col in range(columns_count):
#             palindrome = alpha[row] + alpha[col + row] + alpha[row]
#             result.append(palindrome)
#         the_matrix. append(result)
#     return the_matrix
#
#
# alphabet = list(map(chr, range(97, 123)))
# matrix = matrix_generator(alphabet)

rows_count, columns_count = list(map(int, input().split()))
alphabet = list(map(chr, range(97, 123)))


def columns_builder(row, cols, alpha):
    result = []
    for col in range(cols):
        palindrome = alpha[row] + alpha[col + row] + alpha[row]
        result.append(palindrome)
    return result


def printing_result(result):
    for row in result:
        print(*row)


matrix = [columns_builder(row, columns_count, alphabet) for row in range(rows_count)]
printing_result(matrix)
