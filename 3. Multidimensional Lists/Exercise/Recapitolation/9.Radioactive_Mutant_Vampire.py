def generate_matrix():
    rows = int(input())
    cols = int(input())
    board = []
    for _ in range(rows):
        board.append(list(input()))
    return board


matrix = generate_matrix()
moves = list(reversed(input()))
game_over = False
won = False


def find_player_on_map(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 'P':
                return (x, y)


def make_move(board, row, col):
    global game_over, won
    if row in range(len(board)) and col in range(len(board[row])):
        if matrix[row][col] == 'B':
            game_over = True
        else:
            matrix[row][col] = 'P'
    else:
        won = True

    return row, col


player_position = find_player_on_map(matrix)


def deploy_bunnies():
    global game_over, won
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                if r - 1 in range(len(matrix)):
                    if matrix[r - 1][c] == 'P':
                        game_over = True
                        won = False
                    matrix[r - 1][c] = 'b'
                if r + 1 in range(len(matrix)):
                    if matrix[r + 1][c] == 'P':
                        game_over = True
                        won = False
                    matrix[r + 1][c] = 'b'
                if c + 1 in range(len(matrix[r])):
                    if matrix[r][c + 1] == 'P':
                        game_over = True
                        won = False
                    matrix[r][c + 1] = 'b'
                if c - 1 in range(len(matrix[r])):
                    if matrix[r][c - 1] == 'P':
                        game_over = True
                        won = False
                    matrix[r][c - 1] = 'b'
    for row in matrix:
        for i in range(len(row)):
            if row[i] == 'b':
                row[i] = 'B'


while moves:
    current_move = moves.pop()
    row, col = player_position
    matrix[row][col] = '.'
    if current_move == 'U':
        player_position = make_move(matrix, row - 1, col)
        if won:
            row += 1
    elif current_move == 'D':
        player_position = make_move(matrix, row + 1, col)
        if won:
            row -= 1
    elif current_move == 'L':
        player_position = make_move(matrix, row, col - 1)
        if won:
            col += 1
    else:
        player_position = make_move(matrix, row, col + 1)
        if won:
            col += 1

    deploy_bunnies()

    if game_over or won:
        break

for r in matrix:
    print(f"{''.join(r)}")

if won:
    print(f'won: {player_position[0]} {player_position[1]}')
else:
    print(f'dead: {player_position[0]} {player_position[1]}')
