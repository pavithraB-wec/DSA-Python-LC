class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0.0] * (query_row + 2) for _ in range(query_row + 2)]
        dp[0][0] = float(poured)

        for i in range(query_row):
            for j in range(i + 1):
                overflow = (dp[i][j] - 1.0) / 2.0
                if overflow > 0:
                    dp[i + 1][j] += overflow
                    dp[i + 1][j + 1] += overflow

        return min(1.0, dp[query_row][query_glass])