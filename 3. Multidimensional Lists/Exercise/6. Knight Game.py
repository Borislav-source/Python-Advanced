def matrix_generator():
    the_matrix = []
    for row in range(int(input())):
        the_matrix.append(input())
    return the_matrix


def knight_attack(r, el):
    counter = []
    if r-2 in range(len(matrix)):
        if el - 1 in range(len(matrix[r - 2])) and matrix[r - 2][el - 1] == 'K':
            counter.append(1)
        if el + 1 in range(len(matrix[r - 2])) and matrix[r - 2][el + 1] == 'K':
            counter.append(1)
    if r+2 in range(len(matrix)):
        if el - 1 in range(len(matrix[r + 2])) and matrix[r + 2][el - 1] == 'K':
            counter.append(1)
        if el + 1 in range(len(matrix[r + 2])) and matrix[r + 2][el + 1] == 'K':
            counter.append(1)
    if r-1 in range(len(matrix)):
        if el - 2 in range(len(matrix[r - 1])) and matrix[r - 1][el - 2] == 'K':
            counter.append(1)
        if el + 2 in range(len(matrix[r - 1])) and matrix[r - 1][el + 2] == 'K':
            counter.append(1)
    if r+1 in range(len(matrix)):
        if el - 2 in range(len(matrix[r + 1])) and matrix[r + 1][el - 2] == 'K':
            counter.append(1)
        if el + 2 in range(len(matrix[r + 1])) and matrix[r + 1][el + 2] == 'K':
            counter.append(1)
    return len(counter)


matrix = matrix_generator()
count = 0
while True:
    attacks = 0
    best = 0
    coordinates = ()
    for row in range(len(matrix)):
        for ele in range(len(matrix[row])):
            if matrix[row][ele] == 'K':
                attack = knight_attack(row, ele)
            else:
                continue
            if attack > 0:
                attacks += 1
                if attack > best:
                    best = attack
                    coordinates = row, ele
    if attacks:
        ro, elem = coordinates
        matrix[ro] = matrix[ro][:elem] + '0' + matrix[ro][elem + 1:]
        count += 1
    else:
        break
print(count)
