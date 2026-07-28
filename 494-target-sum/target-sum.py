class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)

        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        subset = (total + target) // 2

        dp = [0] * (subset + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset]