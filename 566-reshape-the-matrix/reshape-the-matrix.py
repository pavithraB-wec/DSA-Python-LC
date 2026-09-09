class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        # Reshape is not possible
        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                index = i * n + j

                new_row = index // c
                new_col = index % c

                result[new_row][new_col] = mat[i][j]

        return result