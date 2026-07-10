class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        if k == i + 1:
                            dp[i][j] = min(dp[i][j], dp[k][j])
                        else:
                            dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j])

        return dp[0][n - 1]