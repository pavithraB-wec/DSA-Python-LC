class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        min_suffix = nums[-1]

        for i in range(n - 3, -1, -1):
            min_suffix = min(min_suffix, nums[i + 2])
            if nums[i] > min_suffix:
                return False

        return True