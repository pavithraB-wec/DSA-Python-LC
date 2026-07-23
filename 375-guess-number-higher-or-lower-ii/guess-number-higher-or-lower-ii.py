class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                dp[start][end] = float('inf')

                for pivot in range(start, end + 1):
                    cost = pivot + max(dp[start][pivot - 1],
                                       dp[pivot + 1][end])
                    dp[start][end] = min(dp[start][end], cost)

        return dp[1][n]