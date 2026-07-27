class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def robLine(houses):
            prev1 = 0
            prev2 = 0

            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        return max(robLine(nums[:-1]), robLine(nums[1:]))