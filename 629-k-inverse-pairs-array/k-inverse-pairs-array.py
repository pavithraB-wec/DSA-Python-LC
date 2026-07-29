class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            new = [0] * (k + 1)
            prefix = 0

            for j in range(k + 1):
                prefix = (prefix + dp[j]) % MOD
                if j >= i:
                    prefix = (prefix - dp[j - i]) % MOD
                new[j] = prefix

            dp = new

        return dp[k]