class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                if i > 0:
                    dp[i][j] |= (
                        dp[i - 1][j] and
                        s1[i - 1] == s3[i + j - 1]
                    )

                if j > 0:
                    dp[i][j] |= (
                        dp[i][j - 1] and
                        s2[j - 1] == s3[i + j - 1]
                    )

        return dp[m][n]