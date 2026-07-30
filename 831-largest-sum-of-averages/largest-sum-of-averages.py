class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [0.0] * n

        # Base case: one partition
        for i in range(n):
            dp[i] = float(prefix[n] - prefix[i]) / (n - i)

        # Add more partitions
        for _ in range(1, k):
            new_dp = dp[:]
            for i in range(n):
                for j in range(i, n - 1):
                    avg = float(prefix[j + 1] - prefix[i]) / (j - i + 1)
                    new_dp[i] = max(new_dp[i], avg + dp[j + 1])
            dp = new_dp

        return dp[0]