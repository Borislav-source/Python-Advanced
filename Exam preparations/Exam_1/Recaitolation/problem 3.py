def build_triangle(n):
    mtrx = []
    for c in range(1, n + 1):
        col = []
        for _ in range(c):
            col.append(1)
        mtrx.append(col)
    return mtrx


def calculating(board):
    for row in range(len(board)):
        if row > 1:
            for col in range(1, len(board[row]) - 1):
                a = board[row - 1][col-1]
                b = board[row - 1][col]
                board[row][col] = a + b
        continue
    return board


def get_magic_triangle(n):
    triangle = build_triangle(n)
    triangle = calculating(triangle)
    return triangle[99]


print(get_magic_triangle(100))
