class Solution(object):
    def matrixBlockSum(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                top = max(0, i - k)
                bottom = min(m - 1, i + k)
                left = max(0, j - k)
                right = min(n - 1, j + k)

                answer[i][j] = (
                    prefix[bottom + 1][right + 1]
                    - prefix[top][right + 1]
                    - prefix[bottom + 1][left]
                    + prefix[top][left]
                )

        return answer