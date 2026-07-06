class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        isPal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (
                    end - start <= 2 or isPal[start + 1][end - 1]
                ):
                    isPal[start][end] = True

        dp = [0] * n

        for i in range(n):

            if isPal[0][i]:
                dp[i] = 0
            else:
                dp[i] = i

                for j in range(i):
                    if isPal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]