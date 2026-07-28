class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(1, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1

                for k in range(left, right + 1):
                    coins = (
                        dp[left][k - 1]
                        + arr[left - 1] * arr[k] * arr[right + 1]
                        + dp[k + 1][right]
                    )
                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][n]