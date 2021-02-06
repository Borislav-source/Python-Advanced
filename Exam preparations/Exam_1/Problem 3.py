
def get_magic_triangle(n, current_row=1, the_matrix=[]):
    if current_row == n + 1:
        for row in range(0, len(the_matrix)):
            if row > 1:
                for col in range(1, len(the_matrix[row]) - 1):
                    the_matrix[row][col] = the_matrix[row - 1][col - 1] + the_matrix[row - 1][col]
        return

    row_list = []
    for _ in range(0, current_row):
        row_list.append(1)
    the_matrix.append(row_list)
    get_magic_triangle(n, current_row + 1, the_matrix)
    return the_matrix




import unittest


class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        actual = get_magic_triangle(5)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
