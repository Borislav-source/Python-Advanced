# def matrix_generator():
#     rows_count = int(input())
#     the_matrix = []
#     for row in range(rows_count):
#         line = input()
#         the_matrix.append(line)
#     return the_matrix
#
#
# matrix = matrix_generator()
# counter = 0
# for r in range(len(matrix)):
#     for el in range(len(matrix[r])):
#         if matrix[r][el] == 'K':
#             if r-2 in range(len(matrix)-1):
#                 if el-1 in range(len(matrix[r-2])-1):
#                     if matrix[r-2][el-1] == 'K':
#                         matrix[r-2] = matrix[r-2][:el-1] + '0' + matrix[r-2][el:]
#                         counter += 1
#                 if el+1 in range(len(matrix[r-2])-1):
#                     if matrix[r-2][el+1] == 'K':
#                         matrix[r-2] = matrix[r-2][:el+1] + '0' + matrix[r-2][el + 2:]
#                         counter += 1
#             if r+2 in range(len(matrix)-1):
#                 if el-1 in range(len(matrix[r + 2])-1):
#                     if matrix[r + 2][el - 1] == 'K':
#                         matrix[r+2] = matrix[r+2][:el-1] + '0' + matrix[r+2][el:]
#                         counter += 1
#                 if el+1 in range(len(matrix[r + 2])-1):
#                     if matrix[r + 2][el + 1] == 'K':
#                         matrix[r+2] = matrix[r+2][:el+1] + '0' + matrix[r+2][el + 2:]
#                         counter += 1
#             if r-1 in range(len(matrix)-1):
#                 if el-2 in range(len(matrix[r-1])-1):
#                     if matrix[r-1][el-2] == 'K':
#                         matrix[r-1] = matrix[r-1][:el-2] + '0' + matrix[r-1][el-1:]
#                         counter += 1
#                 if el+2 in range(len(matrix[r-1])-1):
#                     if matrix[r-1][el+2] == 'K':
#                         matrix[r-1] = matrix[r-1][:el+2] + '0' + matrix[r-1][el + 3:]
#                         counter += 1
#             if r+1 in range(len(matrix)-1):
#                 if el-2 in range(len(matrix[r+1])-1):
#                     if matrix[r+1][el-2] == 'K':
#                         matrix[r+1] = matrix[r+1][:el-2] + '0' + matrix[r+1][el-1:]
#                         counter += 1
#                 if el+2 in range(len(matrix[r+1])-1):
#                     if matrix[r+1][el+2] == 'K':
#                         matrix[r+1] = matrix[r+1][:el+2] + '0' + matrix[r+1][el + 3:]
#                         counter += 1
#
# print(counter)
#
#
# nums = []
# a = 5
# b = 6
# nums.append([a, b])
# print(nums)

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
a[1][0] += 1
print(a)
