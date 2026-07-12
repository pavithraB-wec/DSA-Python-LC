class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_index = {}

        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True

            last_index[num] = i

        return False