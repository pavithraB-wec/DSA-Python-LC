class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        row_max = [max(row) for row in grid]

        col_max = [0] * n
        for j in range(n):
            for i in range(n):
                col_max[j] = max(col_max[j], grid[i][j])

        ans = 0

        for i in range(n):
            for j in range(n):
                new_height = min(row_max[i], col_max[j])
                ans += new_height - grid[i][j]

        return ans