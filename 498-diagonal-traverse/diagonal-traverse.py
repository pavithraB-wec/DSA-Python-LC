class Solution(object):
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])

        result = []

        row = 0
        col = 0
        direction = 1

        for _ in range(m * n):
            result.append(mat[row][col])

            if direction == 1:
                # Moving up-right
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1

            else:
                # Moving down-left
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result