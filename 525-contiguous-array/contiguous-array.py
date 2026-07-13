class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        first_index = {0: -1}
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in first_index:
                max_len = max(max_len, i - first_index[count])
            else:
                first_index[count] = i

        return max_len