class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual