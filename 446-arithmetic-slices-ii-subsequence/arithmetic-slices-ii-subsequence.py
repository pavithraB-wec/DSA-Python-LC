class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [dict() for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j].get(diff, 0)

                dp[i][diff] = dp[i].get(diff, 0) + count + 1
                ans += count

        return ans