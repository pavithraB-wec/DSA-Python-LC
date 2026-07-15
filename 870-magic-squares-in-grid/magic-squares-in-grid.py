class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        if rows < 3 or cols < 3:
            return 0

        def isMagic(r, c):
            nums = []

            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9:
                        return False
                    nums.append(val)

            if len(set(nums)) != 9:
                return False

            # Rows
            for i in range(3):
                if sum(grid[r + i][c:c + 3]) != 15:
                    return False

            # Columns
            for j in range(3):
                if (grid[r][c + j] +
                    grid[r + 1][c + j] +
                    grid[r + 2][c + j]) != 15:
                    return False

            # Diagonals
            if (grid[r][c] +
                grid[r + 1][c + 1] +
                grid[r + 2][c + 2]) != 15:
                return False

            if (grid[r][c + 2] +
                grid[r + 1][c + 1] +
                grid[r + 2][c]) != 15:
                return False

            return True

        ans = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    ans += 1

        return ans