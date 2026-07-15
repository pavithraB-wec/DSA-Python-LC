class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        arr.sort()
        dp = {}
        index = {}

        for i, x in enumerate(arr):
            index[x] = i
            dp[x] = 1

        for i, x in enumerate(arr):
            for j in range(i):
                a = arr[j]

                if x % a == 0:
                    b = x // a

                    if b in dp:
                        dp[x] = (dp[x] + dp[a] * dp[b]) % MOD

        return sum(dp.values()) % MOD