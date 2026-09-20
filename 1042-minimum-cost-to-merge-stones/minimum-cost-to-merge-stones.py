class Solution(object):
    def mergeStones(self, stones, k):
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        INF = 10 ** 18

        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                best = INF

                # Split at positions that preserve valid pile counts
                for mid in range(left, right, k - 1):
                    best = min(
                        best,
                        dp[left][mid] + dp[mid + 1][right]
                    )

                dp[left][right] = best

                # If this interval can be merged into one pile
                if (length - 1) % (k - 1) == 0:
                    dp[left][right] += (
                        prefix[right + 1] - prefix[left]
                    )

        return dp[0][n - 1]