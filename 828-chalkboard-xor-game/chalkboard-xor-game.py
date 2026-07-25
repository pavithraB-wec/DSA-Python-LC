class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        xor = 0
        for num in nums:
            xor ^= num

        return xor == 0 or len(nums) % 2 == 0