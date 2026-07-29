class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        memo = {}

        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2

            if (r1 >= n or c1 >= n or
                r2 >= n or c2 >= n or
                grid[r1][c1] == -1 or
                grid[r2][c2] == -1):
                return float('-inf')

            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            key = (r1, c1, r2)
            if key in memo:
                return memo[key]

            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            best = max(
                dp(r1 + 1, c1, r2 + 1),
                dp(r1 + 1, c1, r2),
                dp(r1, c1 + 1, r2 + 1),
                dp(r1, c1 + 1, r2)
            )

            memo[key] = cherries + best
            return memo[key]

        return max(0, dp(0, 0, 0))