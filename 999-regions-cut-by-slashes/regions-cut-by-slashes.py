class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        size = n * 3
        mat = [[0] * size for _ in range(size)]

        # Expand each cell into a 3x3 block
        for i in range(n):
            for j in range(n):
                r = i * 3
                c = j * 3

                if grid[i][j] == '/':
                    mat[r][c + 2] = 1
                    mat[r + 1][c + 1] = 1
                    mat[r + 2][c] = 1

                elif grid[i][j] == '\\':
                    mat[r][c] = 1
                    mat[r + 1][c + 1] = 1
                    mat[r + 2][c + 2] = 1

        def dfs(x, y):
            stack = [(x, y)]
            mat[x][y] = 1

            while stack:
                i, j = stack.pop()

                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni = i + dx
                    nj = j + dy

                    if (0 <= ni < size and
                        0 <= nj < size and
                        mat[ni][nj] == 0):
                        mat[ni][nj] = 1
                        stack.append((ni, nj))

        regions = 0

        for i in range(size):
            for j in range(size):
                if mat[i][j] == 0:
                    regions += 1
                    dfs(i, j)

        return regions