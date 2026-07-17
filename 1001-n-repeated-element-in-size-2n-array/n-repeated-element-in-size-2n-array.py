class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)