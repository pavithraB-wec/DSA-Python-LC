class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for bit in range(32):
            ones = 0

            for num in nums:
                if (num >> bit) & 1:
                    ones += 1

            ans += ones * (n - ones)

        return ans