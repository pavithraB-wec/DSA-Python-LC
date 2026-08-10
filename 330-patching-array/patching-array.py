class Solution(object):
    def minPatches(self, nums, n):
        miss = 1
        i = 0
        patches = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # Patch with 'miss'
                miss += miss
                patches += 1

        return patches