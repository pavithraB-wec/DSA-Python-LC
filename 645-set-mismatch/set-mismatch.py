class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = -1
        missing = -1

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicate = abs(num)
            else:
                nums[idx] = -nums[idx]

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]