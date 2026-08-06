class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1

            while left < right and nums[right] % 2 == 1:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]

        return nums