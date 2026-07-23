class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)

        f = 0
        for i in range(n):
            f += i * nums[i]

        ans = f

        for k in range(1, n):
            f = f + total - n * nums[n - k]
            ans = max(ans, f)

        return ans