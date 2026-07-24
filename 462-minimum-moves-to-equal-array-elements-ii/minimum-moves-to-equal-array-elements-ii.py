class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) // 2]

        moves = 0
        for num in nums:
            moves += abs(num - median)

        return moves