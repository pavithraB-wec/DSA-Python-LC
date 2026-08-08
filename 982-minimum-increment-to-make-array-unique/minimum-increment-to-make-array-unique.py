class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1
                moves += needed - nums[i]
                nums[i] = needed
                
        return moves