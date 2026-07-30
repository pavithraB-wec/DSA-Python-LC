class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        banned = set(map(tuple, mines))
        dp = [[n] * n for _ in range(n)]

        # Left and Right
        for i in range(n):
            count = 0
            for j in range(n):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j], count)

            count = 0
            for j in range(n - 1, -1, -1):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j], count)

        ans = 0

        # Up and Down
        for j in range(n):
            count = 0
            for i in range(n):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j], count)

            count = 0
            for i in range(n - 1, -1, -1):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j], count)
                ans = max(ans, dp[i][j])

        return ans