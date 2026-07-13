class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] = -nums[idx]

        return result